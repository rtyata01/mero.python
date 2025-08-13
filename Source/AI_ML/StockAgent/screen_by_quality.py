# Screen the high quality stocks (short term gains)
# 1. Technical Indicators
    # Measures overbought (RSI > 70) or oversold (RSI < 30) conditions to predict short-term price reversals or continuations.
    # RSI 30–70 (neutral, indicating potential for growth without overbought risk).
    # Avoid overbought stocks (RSI > 70) to reduce risk of corrections in long-term holdings.
# 2. Moving Average Convergence Divergence (MACD)
    # A bullish crossover (MACD line crosses above signal line) signals a buy for short-term gains.
    # Confirms uptrends for sustained growth when MACD remains above zero.
# 3. Bollinger Bands:
    # Prices touching the upper band with rising volume suggest a breakout.
# 4. Revenue Growth:
    # Consistent revenue growth > 10%
# 5. Earnings Quality
    # Consistently beat earnings expectations
    
import time
import random
import logging
import backoff
import sqlite3
import pandas as pd
import numpy as np
import yfinance as yf
from typing import List, Tuple, Optional
from contextlib import contextmanager
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
from screener_utils import init_cache_db, get_stock_history, save_stock_history, load_trending_tickers

# --- Configuration ---
DATA_DIR = "data"
DB_NAME = "stock_data_cache.db"
MAX_WORKERS = 5
LOOKBACK_DAYS = 60
DATE_FORMAT = "%Y-%m-%d"
DEFAULT_TRENDING_STOCKS = ["NIO","TSLA","NVDA","AMD","PLTR", "SOFI", "SMCI", "MSFT", "GOOGL", "AMZN", "AAPL"]

# --- Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Context Managers ---
@contextmanager
def db_connection():
    db_path = Path(__file__).resolve().parent / DATA_DIR / DB_NAME
    conn = sqlite3.connect(db_path)
    try:
        yield conn
    finally:
        conn.close()

# --- Indicators ---

def calculate_rsi(hist, short: int = 14):
    """Calculate 14-day RSI for the stock."""
    if not isinstance(hist, pd.DataFrame) or hist.empty:
        return None
    try:
        close_prices = hist['Close']
        deltas = close_prices.diff().dropna()
        gains = deltas.where(deltas > 0, 0).rolling(short).mean()
        losses = -deltas.where(deltas < 0, 0).rolling(short).mean()
        rs = gains / losses
        rsi = 100 - (100 / (1 + rs))
        return rsi.iloc[-1]
    except Exception as e:
        logger.warning(f"Error calculating RSI: {str(e)}")
        return None
    
def calculate_macd(hist, short: int = 12, long: int = 26, signal: int = 9) -> bool:
    """Check if MACD indicates a bullish crossover."""
    if not isinstance(hist, pd.DataFrame) or hist.empty or len(hist) < long + signal:
        return False
    try:
        close_prices = hist['Close']
        short_ema = close_prices.ewm(span=short, adjust=False).mean()
        long_ema = close_prices.ewm(span=long, adjust=False).mean()
        macd = short_ema - long_ema
        signal = macd.ewm(span=signal, adjust=False).mean()
        return macd.iloc[-1] > signal.iloc[-1] and macd.iloc[-2] <= signal.iloc[-2]  # Bullish crossover
    except Exception as e:
        logger.warning(f"Error calculating MACD: {str(e)}")
        return False
    
def calculate_bollinger_bands(hist: pd.DataFrame, period: int = 20, std_dev: float = 2.0) -> bool:
    """Check if price is above upper Bollinger Band for breakout."""
    if not isinstance(hist, pd.DataFrame) or hist.empty or len(hist) < period:
        return False
    try:
        close_prices = hist['Close']
        sma = close_prices.rolling(window=period).mean()
        std = close_prices.rolling(window=period).std()
        upper_band = sma + (std * std_dev)
        return close_prices.iloc[-1] > upper_band.iloc[-1]
    except Exception as e:
        logger.warning(f"Error calculating Bollinger Bands: {str(e)}")
        return False
    
def calculate_revenue_growth(stock: yf.Ticker) -> float:
    try:
        financials = stock.quarterly_financials
        if financials.empty or len(financials.index) < 4:
            return None
        latest_revenue = financials.loc["Total Revenue"].iloc[0]
        yoy_revenue = financials.loc["Total Revenue"].iloc[4]
        if latest_revenue and yoy_revenue and yoy_revenue > 0:
            return (latest_revenue - yoy_revenue) / yoy_revenue * 100
        return None
    except Exception as e:
        logger.warning(f"Error calculating revenue growth: {str(e)}")
        return None
    
def check_earnings_surprise(ticker: str, stock: yf.Ticker, min_surprise_pct: float = 5.0, quarters: int = 1) -> bool:
    """
    Checks if the latest EPS actual was significantly greater than the EPS estimate (positive surprise).
    Returns:
        bool: True if the stock has a significant positive earnings surprise in the specified quarters.
    """
    try:
        earnings_df = stock.earnings_dates
        if earnings_df is None or earnings_df.empty or len(earnings_df) < quarters:
            logger.warning(f"No or insufficient earnings data for {ticker}")
            return False

        # Check the most recent 'quarters' rows
        for i in range(min(quarters, len(earnings_df))):
            latest = earnings_df.iloc[i]
            if "EPS Estimate" not in latest or "Reported EPS" not in latest:
                logger.warning(f"Missing EPS data for {ticker} in quarter {i+1}")
                return False

            eps_estimate = latest["EPS Estimate"]
            eps_actual = latest["Reported EPS"]

            if pd.isna(eps_estimate) or pd.isna(eps_actual):
                logger.warning(f"Null EPS data for {ticker} in quarter {i+1}")
                return False

            if eps_estimate <= 0:  # Avoid division by zero or negative estimates
                logger.warning(f"Invalid EPS estimate ({eps_estimate}) for {ticker}")
                return False

            surprise_pct = (eps_actual - eps_estimate) / eps_estimate * 100
            if surprise_pct <= min_surprise_pct:
                logger.info(f"Earnings surprise for {ticker} ({surprise_pct:.2f}%) below threshold ({min_surprise_pct}%)")
                return False

        logger.info(f"Positive earnings surprise for {ticker}: {surprise_pct:.2f}%")
        return True

    except Exception as e:
        logger.warning(f"Error checking earnings surprise for {ticker}: {str(e)}")
        return False
    
def sleep_with_jitter(min_delay=1, max_delay=3):
    """Add delay with jitter to avoid triggering rate limits."""
    time.sleep(random.uniform(min_delay, max_delay))

@backoff.on_exception(
    backoff.expo,
    (Exception,),
    max_tries=5,
    jitter=backoff.full_jitter,
    giveup=lambda e: "404" in str(e) or "Not Found" in str(e)
)
    
def safe_fetch_stock_data(stock: yf.Ticker, start, end):
    """Safe wrapper to fetch stock data with retries."""
    return stock.history(start=start, end=end, interval="1d", auto_adjust=True)

def compute_quality_score(ticker, hist, stock: yf.Ticker):
    """Predict fundamental score greater than 4 out of 6, will be likely good"""
    score = 0

    revenue_growth = calculate_revenue_growth(stock)
    if isinstance(revenue_growth, (int, float)) and revenue_growth > 0.1:
        score += 1

    earnings_surprise = check_earnings_surprise(ticker, stock)
    if earnings_surprise:
        score += 1

    rsi_value = calculate_rsi(hist)
    if 30 < rsi_value < 70:
        score += 1

    bullish_crossover = calculate_macd(hist)
    if bullish_crossover:
        score += 1
        
    breakout_signals = calculate_bollinger_bands(hist)
    if breakout_signals:
        score += 1

    return score

def get_quality_stocks(
    ticker: str,
    lookback_days: int = LOOKBACK_DAYS,
) -> Tuple[bool, Optional[str], Optional[float], Optional[int]]:

    try:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=lookback_days + 1)
        hist = get_stock_history(ticker, start_date, end_date)

        last_cached = hist.index.max() if not hist.empty else None

        stock = yf.Ticker(ticker)
        sleep_with_jitter()  # Delay after each API call
        
        stock_name = stock.info.get("longName", "N/A")

        # Fetch missing data if needed
        if not last_cached or last_cached.date() < (end_date - timedelta(days=1)).date():
            fetch_start = last_cached if last_cached else start_date
            try:
                new_data = safe_fetch_stock_data(stock, fetch_start, end_date)
                if not new_data.empty:
                    save_stock_history(ticker, new_data)
                    hist = get_stock_history(ticker, start_date, end_date)
                sleep_with_jitter()  # Delay after each API call
            except Exception as e:
                logger.debug(f"{ticker} fetch failed: {e}")
                return False, stock_name, None, None

        latest_volume = int(hist['Volume'].iloc[-1]) if not hist.empty else None
        latest_price = hist['Close'].iloc[-1] if not hist.empty else None
        quality_score = compute_quality_score(ticker, hist, stock)
        
        return quality_score, stock_name, latest_price, latest_volume

    except Exception as e:
        logger.warning(f"Error checking {ticker}: {e}")
        return False, ticker, None, None

def find_quality_stocks(max_workers: int = MAX_WORKERS, monthly_screen: bool = False) -> List[Tuple[str, str, Optional[float], Optional[int], bool]]:
    """Find stocks with better quality."""
    tickers_to_screen = load_trending_tickers()
    results = []
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(get_quality_stocks, ticker): ticker for ticker in tickers_to_screen}
        for future in as_completed(futures):
            ticker = futures[future]
            try:
                trending_score, name, price, volume = future.result()
                if trending_score >= 4:
                    results.append((ticker, name, price, volume, trending_score))
            except Exception as err:
                logger.warning(f"Error processing {ticker}: {err}")

    logger.info(f"Found {len(results)} trending stocks")
    return sorted(results, key=lambda x: x[0])

def save_quality_tickers_to_db(ticker_data: List[Tuple[str, str, Optional[float], Optional[int], bool]]):
    """Insert or update high-volume tickers in DB."""
    try:
        with db_connection() as conn:
            cursor = conn.cursor()
        
            # Reset the has_rising_volume field for all stocks
            cursor.execute("UPDATE eligible_stocks SET quality_score = CAST(0 AS INTEGER)")
            
            # Prepare data for bulk insert (only those with rising volume)
            data_to_insert = [
                (symbol, name, price, volume, score)
                for symbol, name, price, volume, score in ticker_data
            ]
            
            if data_to_insert:
                # Bulk insert using executemany
                cursor.executemany("""
                    INSERT OR REPLACE INTO eligible_stocks (symbol, stock_name, price, volume, quality_score)
                    VALUES (?, ?, ?, ?, ?)
                """, data_to_insert)
                
                # Commit all changes in one transaction
                conn.commit()
                logger.info(f"{len(data_to_insert)} stocks with quality stockes saved to database.")
            else:
                logger.info("No stocks with better quality to insert.")
    except Exception as e:
        logger.error(f"Database insert failed: {e}")
        raise RuntimeError("DB insert failed") from e


# --- Main Execution ---
if __name__ == "__main__":
    try:
        init_cache_db()
        logger.info("Screening quality stocks ...")
        tickers = find_quality_stocks()
        save_quality_tickers_to_db(tickers)
        logger.info(f"Found {len(tickers)} quality stocks.")
    except Exception as main_err:
        logger.error(f"Fatal error: {main_err}")
        print(f"Error: {main_err}")