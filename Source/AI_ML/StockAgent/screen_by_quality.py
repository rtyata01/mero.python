# Screen high-quality stocks for short-term gains
# This uses a combination of technical indicators, fundamental metrics, earnings performance, and market sentiment
# to identify stocks with strong potential for high-quality short-term gains.

# 1. Technical Indicators
#    - Relative Strength Index (RSI):
#      Measures overbought (RSI > 70) or oversold (RSI < 30) conditions.
#      RSI 30–70 indicates a neutral zone, signaling potential growth without overbought risk.
#      Avoid overbought stocks (RSI > 70) to reduce risk of short-term corrections.
#
#    - Moving Average Convergence Divergence (MACD):
#      A bullish crossover (MACD line crosses above signal line) signals a buy for short-term gains.
#      Sustained MACD above zero confirms an ongoing uptrend.
#
#    - Bollinger Bands:
#      Price touching or exceeding the upper band with rising volume suggests a breakout opportunity.
#
#    - Average True Range (ATR):
#      Measures stock volatility. Higher ATR indicates higher price movement, useful for breakout and risk analysis.
#
#    - Order Book Ratio (OBR):
#      Ratio of buy vs sell orders; higher OBR indicates stronger buying pressure in the market.
#
# 2. Fundamental Metrics
#    - Revenue Growth:
#      Consistent quarterly revenue growth > 10% signals strong operational performance.
#
#    - Earnings Quality:
#      Consistently beats analyst EPS estimates (positive earnings surprise), indicating reliable profitability.
    
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
from screener_utils import init_cache_db, get_stock_history, save_stock_history, load_trending_tickers, DEFAULT_TRENDING_STOCKS

# --- Configuration ---
DATA_DIR = "data"
DB_NAME = "stock_data_cache.db"
MAX_WORKERS = 5
LOOKBACK_DAYS = 60  # ~12 weeks
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

# --- Technical Indicators ---

def calculate_rsi(hist: pd.DataFrame, period: int = 14) -> Optional[float]:
    """14-day RSI"""
    if hist.empty or 'Close' not in hist:
        return None
    delta = hist['Close'].diff().dropna()
    gain = delta.where(delta > 0, 0).rolling(period).mean()
    loss = -delta.where(delta < 0, 0).rolling(period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi.iloc[-1] if not rsi.empty else None
        
def calculate_macd(hist: pd.DataFrame, short: int = 12, long: int = 26, signal_period: int = 9) -> bool:
    """MACD bullish crossover confirmed above zero line"""
    if hist.empty or len(hist) < long + signal_period:
        return False
    close = hist['Close']
    short_ema = close.ewm(span=short, adjust=False).mean()
    long_ema = close.ewm(span=long, adjust=False).mean()
    macd_line = short_ema - long_ema
    signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()
    # Bullish crossover & MACD above zero
    return macd_line.iloc[-1] > signal_line.iloc[-1] and macd_line.iloc[-2] <= signal_line.iloc[-2] and macd_line.iloc[-1] > 0

def calculate_bollinger_band_breakout(hist: pd.DataFrame, period: int = 20, std_dev: float = 2.0) -> bool:
    """Check if price above upper BB with rising volume"""
    if hist.empty or len(hist) < period or 'Close' not in hist or 'Volume' not in hist:
        return False
    close = hist['Close']
    volume = hist['Volume']
    sma = close.rolling(period).mean()
    std = close.rolling(period).std()
    upper = sma + std_dev * std
    # Require price above upper band and rising volume last 3 periods
    volume_rising = volume.iloc[-3:].is_monotonic_increasing
    return close.iloc[-1] > upper.iloc[-1] and volume_rising

def calculate_obv(hist) -> bool:
    """On Balance Volume trend confirmation"""
    if hist.empty: 
        return False
    obv = (np.sign(hist['Close'].diff()) * hist['Volume']).fillna(0).cumsum()
    
    return obv.iloc[-1] > obv.iloc[-5:].mean()  # Trend positive

def calculate_atr(hist, period=14) -> Optional[float]:
    """Average True Range (volatility)"""
    if hist.empty or len(hist) < period: 
        return None
    
    # Use absolute daily price change as a proxy
    tr = hist['Close'].diff().abs()
    
    atr = tr.rolling(period).mean()
    return atr.iloc[-1] if not atr.empty else None

# --- Fundamental / Quality Signals ---

def calculate_revenue_growth(stock: yf.Ticker, quarters: int = 4) -> Optional[float]:
    """Check multi-quarter revenue growth consistency"""
    try:
        fin = stock.quarterly_financials
        if fin.empty or len(fin.columns) < quarters:
            return None
        revenues = fin.loc["Total Revenue"].head(quarters)
        growth = [(revenues[i] - revenues[i+1])/revenues[i+1] for i in range(len(revenues)-1) if revenues[i+1] != 0]
        if not growth:
            return None
        return sum(growth)/len(growth)
    except Exception:
        return None
    
def check_earnings_surprise(stock: yf.Ticker, quarters: int = 2, min_pct: float = 5.0) -> bool:
    """Check multiple quarters of positive EPS surprise"""
    try:
        df = stock.earnings_dates
        if df is None or len(df) < quarters:
            return False
        for i in range(min(quarters, len(df))):
            row = df.iloc[i]
            est, act = row.get("EPS Estimate"), row.get("Reported EPS")
            if est is None or act is None or est <= 0:
                return False
            surprise_pct = (act - est) / est * 100
            if surprise_pct < min_pct:
                return False
        return True
    except Exception:
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
    """Calculate a weighted technical and quality score (out of 10) for a stock."""
    score = 0.0
    
    # Fundamental: revenue growth > 10%
    rev_growth = calculate_revenue_growth(stock)
    if rev_growth and rev_growth > 0.1:
        score += 1.5  # higher weight
    
    # Fundamental: consistent earnings surprise
    if check_earnings_surprise(stock):
        score += 2.0  # higher weight
    
    # Technical: RSI neutral (30-70)
    rsi_val = calculate_rsi(hist)
    if rsi_val and 30 < rsi_val < 70:
        score += 1.0
    
    # Technical: MACD bullish crossover
    if calculate_macd(hist):
        score += 2.0
    
    # Technical: Bollinger breakout with volume
    if calculate_bollinger_band_breakout(hist):
        score += 1.0
        
    # OBV trend
    if calculate_obv(hist): 
        score += 1.0
    
    # ATR moderate volatility
    atr = calculate_atr(hist)
    if atr and atr < hist['Close'].iloc[-1] * 0.05:  # 5% ATR threshold
        score += 1.5

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
                if trending_score >= 7: # strong threshold for high-quality
                    results.append((ticker, name, price, volume, trending_score))
            except Exception as err:
                logger.warning(f"Error processing {ticker}: {err}")

    logger.info(f"Found {len(results)} high quality stocks")
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
        logger.info("Screening high-quality stocks ...")
        tickers = find_quality_stocks()
        save_quality_tickers_to_db(tickers)
        logger.info(f"Found {len(tickers)} high-quality stocks.")
    except Exception as main_err:
        logger.error(f"Fatal error: {main_err}")
        print(f"Error: {main_err}")