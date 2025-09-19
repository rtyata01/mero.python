# Screen and identify stocks with strong fundamentals and statistically significant trading activity.
#
# Scoring components:
#     1. EPS > 0 (weight=2)
#     2. ROE > industry_avg_roe (weight=2)
#     3. Debt/Equity < industry_avg_debt_to_equity (weight=1)
#     4. P/E ratio < industry_avg_pe (weight=1)
#     5. Price trend: high-confidence monthly increases (weight=2)
#     6. Volume trend: recent volume spike (weight=2)
#
# Interpretation:
# - Stocks with fundamental score >= 4 are considered likely strong candidates.
# - Price trend uses percentage of increasing months (high-confidence if >= 75% months increase)
# - Volume trend uses percentile (e.g., 80th percentile) or z-score thresholds for significance
# - Filtering ensures sufficient liquidity and reduces noisy or illiquid stocks from consideration.

import time
import random
import logging
import backoff
import sqlite3
import pandas as pd
import numpy as np
import yfinance as yf
from ftplib import FTP
from io import BytesIO
from csv import DictReader
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
VOLUME_PERCENTILE_THRESHOLD = 80.0    # e.g. today's volume must exceed the 80th percentile
PRICE_INCREASE_THRESHOLD = 0.75  # 75% of months must show increasing average price
DATE_FORMAT = "%Y-%m-%d"

# --- Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Context Managers ---

@contextmanager
def ftp_connection(host: str) -> FTP:
    ftp = FTP(host)
    try:
        ftp.login()
        yield ftp
    finally:
        ftp.quit()

@contextmanager
def db_connection():
    db_path = Path(__file__).resolve().parent / DATA_DIR / DB_NAME
    conn = sqlite3.connect(db_path)
    try:
        yield conn
    finally:
        conn.close()

# --- Helper Functions ---

def get_tickers_to_screen_monthly() -> List[str]:
    """Fetch list of active NASDAQ tickers."""
    try:
        with ftp_connection('ftp.nasdaqtrader.com') as ftp:
            buffer = BytesIO()
            ftp.retrbinary('RETR SymbolDirectory/nasdaqlisted.txt', buffer.write)
            buffer.seek(0)
            reader = DictReader(buffer.read().decode('utf-8').splitlines(), delimiter='|')
            tickers = [
                row["Symbol"].upper().strip()
                for row in reader
                if row.get("Test Issue") == "N" and row.get("Financial Status") == "N"
            ]
            
            # Append the default trending stocks
            tickers.extend(DEFAULT_TRENDING_STOCKS)
            return sorted(set(tickers))
    except Exception as e:
        msg = f"FTP connection failed: {e}"
        logger.error(msg)
        raise ConnectionError(msg)

def has_incrementing_monthly_prices(hist: pd.DataFrame, lookback_days: int = LOOKBACK_DAYS) -> bool:
    """
    Check if monthly average prices are increasing for the majority of months.
    Considered high-confidence if >= PRICE_INCREASE_THRESHOLD of months show increase.
    """
    if hist.empty or 'Close' not in hist:
        return False
    try:
        # Align to last N trading days
        close_prices = hist['Close'].dropna().iloc[-lookback_days:]
        if len(close_prices) < lookback_days * 0.6:  # require at least 60% of days
            return False

        # Resample to monthly mean prices
        monthly_prices = close_prices.resample('M').mean()
        if len(monthly_prices) < 2:
            return False

        # Calculate percent of increasing months
        increases = (monthly_prices.diff().dropna() > 0).sum()
        percent_increasing = increases / (len(monthly_prices) - 1)

        return percent_increasing >= PRICE_INCREASE_THRESHOLD
    except Exception:
        return False
    
# --- Improved Volume Trend ---
def has_high_volume_trend(hist: pd.DataFrame, lookback_days: int = LOOKBACK_DAYS) -> bool:
    """
    Check if recent trading volume is statistically significant.
    - Recent volume must exceed the Nth percentile of historical volume.
    - Uses last `lookback_days` trading days.
    """
    if hist.empty or 'Volume' not in hist or hist['Volume'].isnull().all():
        return False
    try:
        volume_data = hist['Volume'].dropna().iloc[-lookback_days:]
        if len(volume_data) < lookback_days * 0.6:  # require at least 60% of days
            return False

        # Percentile-based threshold
        threshold = np.percentile(volume_data, VOLUME_PERCENTILE_THRESHOLD)
        latest_volume = volume_data.iloc[-1]

        # Optionally, also consider z-score
        z_score = (latest_volume - volume_data.mean()) / (volume_data.std() + 1e-6)
        is_significant = latest_volume > threshold or z_score > 2.0  # 95% confidence

        return is_significant
    except Exception:
        return False
    
def sleep_with_jitter(min_delay=0.5, max_delay=1.5):
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

def get_fundamental_score(ticker, hist, stock: yf.Ticker):
    """Calculate a weighted fundamental score (out of 10) for a stock."""
    score = 0.0
    industry_avg_roe = 0.15
    industry_avg_debt_to_equity = 1.0
    industry_avg_pe = 25.0
    
    #logger.info(f"Processing fundamental score for {ticker}!")
    eps = stock.info.get("trailingEps", None)
    if isinstance(eps, (int, float)) and eps > 0:
        score += 2.0

    roe = stock.info.get("returnOnEquity", None)
    if isinstance(roe, (int, float)) and roe > industry_avg_roe:
        score += 2.0

    debt_to_equity = stock.info.get("debtToEquity", None)
    if isinstance(debt_to_equity, (int, float)) and (debt_to_equity * 0.01) < industry_avg_debt_to_equity:
        score += 1.0

    pe_ratio = stock.info.get("trailingPE", None)
    if isinstance(pe_ratio, (int, float)) and pe_ratio < industry_avg_pe:
        score += 1.0

    if has_incrementing_monthly_prices(hist):
        score += 2.0

    if has_high_volume_trend(hist):
        score += 2.0

    return score

def get_trending_stocks(
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
        fundamental_score = get_fundamental_score(ticker, hist, stock)
        
        return fundamental_score, stock_name, latest_price, latest_volume

    except Exception as e:
        logger.warning(f"Error checking {ticker}: {e}")
        return False, ticker, None, None

def find_trending_stocks(tickers = None, max_workers: int = MAX_WORKERS, monthly_screen: bool = False) -> List[Tuple[str, str, Optional[float], Optional[int], bool]]:
    """Find stocks with volume surge based on moving average."""
    tickers_to_screen = []
    results = []
    
    if tickers:
        tickers_to_screen = tickers
    elif monthly_screen:
        tickers_to_screen = get_tickers_to_screen_monthly()
    else:
        tickers_to_screen = load_trending_tickers()
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(get_trending_stocks, ticker): ticker for ticker in tickers_to_screen}
        for future in as_completed(futures):
            ticker = futures[future]
            try:
                trending_score, name, price, volume = future.result()
                if trending_score >= 7:  # strong threshold for fundamentals.
                    results.append((ticker, name, price, volume, trending_score))
            except Exception as err:
                logger.warning(f"Error processing {ticker}: {err}")

    logger.info(f"Found {len(results)} trending stocks")
    return sorted(results, key=lambda x: x[0])

def save_trending_tickers_to_db(ticker_data: List[Tuple[str, str, Optional[float], Optional[int], bool]]):
    """Insert or update high-volume tickers in DB."""
    try:
        with db_connection() as conn:
            cursor = conn.cursor()
        
            # Reset the has_rising_volume field for all stocks
            cursor.execute("UPDATE eligible_stocks SET fundamental_score = CAST(0 AS INTEGER)")
            
            # Prepare data for bulk insert (only those with rising volume)
            data_to_insert = [
                (symbol, name, price, volume, score)
                for symbol, name, price, volume, score in ticker_data
            ]
            
            if data_to_insert:
                # Bulk insert using executemany
                cursor.executemany("""
                    INSERT OR REPLACE INTO eligible_stocks (symbol, stock_name, price, volume, fundamental_score)
                    VALUES (?, ?, ?, ?, ?)
                """, data_to_insert)
                
                # Commit all changes in one transaction
                conn.commit()
                logger.info(f"{len(data_to_insert)} stocks with rising volume saved to database.")
            else:
                logger.info("No stocks with rising volume to insert.")
    except Exception as e:
        logger.error(f"Database insert failed: {e}")
        raise RuntimeError("DB insert failed") from e

# --- Main Execution ---
if __name__ == "__main__":
    try:
        init_cache_db()
        logger.info("Screening trending stocks ...")
        tickers = find_trending_stocks(monthly_screen=False)
        save_trending_tickers_to_db(tickers)
        logger.info(f"Found {len(tickers)} trending stocks.")
    except Exception as main_err:
        logger.error(f"Fatal error: {main_err}")
        print(f"Error: {main_err}")