# Screen the high volume stocks
# The average volume exceeds the baseline (e.g., 25th percentile of history)
# The latest volume exceeds mean + N × std_dev (statistically significant), where N = 2 (95% confidence) or N = 3 (99.7% confidence)
# The latest volume exceeds the percentile threshold (80th Percentile)

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
LOOKBACK_DAYS = 90
VOLUME_PERCENTILE_THRESHOLD = 80.0    # e.g. today's volume must exceed the 80th percentile
MIN_AVERAGE_PERCENTILE = 25.0         # e.g. filter out lowest 25% volume days dynamically
STD_DEV_MULTIPLIER = 2.0              # require volume > mean + 2·std_dev
DATE_FORMAT = "%Y-%m-%d"

# --- Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- DB Connection ---
@contextmanager
def db_connection():
    db_path = Path(__file__).resolve().parent / DATA_DIR / DB_NAME
    conn = sqlite3.connect(db_path)
    try:
        yield conn
    finally:
        conn.close()

# --- Save Ticker Data ---
def save_volume_tickers_to_db(tickers_data: List[Tuple[str, str, Optional[float], Optional[int], bool]]):
    """Insert or update high-volume tickers in DB."""
    try:
        with db_connection() as conn:
            cursor = conn.cursor()
            
             # Reset the has_rising_volume field for all stocks
            cursor.execute("UPDATE eligible_stocks SET has_rising_volume = CAST(0 AS INTEGER)")
            
             # Prepare data for batch update (only symbols with rising prices)
            updates = [(1, symbol) for symbol, _, _, _, is_rising in tickers_data if is_rising]

            if updates:
                cursor.executemany("""
                    UPDATE eligible_stocks
                    SET has_rising_volume = ?
                    WHERE symbol = ?
                """, updates)
                
                conn.commit()
                logger.info(f"Updated {len(updates)} tickers with rising volume.")
            else:
                logger.info("No tickers with rising volume to update.")
    except Exception as e:
        logger.error(f"Database insert failed: {e}")
        raise RuntimeError("DB insert failed") from e

def has_high_confidence_spike(hist: pd.DataFrame) -> Tuple[Optional[int], Optional[float]]:
    """Calculate high confidence spike from volume history."""
    if hist.empty or len(hist) < 2:
        return None, False
    
    # Exclude the latest day for historical stats
    historical_volumes = hist['Volume'].iloc[:-1]
    latest_volume = int(hist['Volume'].iloc[-1])
    avg_volume = historical_volumes.mean()
    std_volume = historical_volumes.std()
    
     # Calculate min_avg_volume_default dynamically as the percentile of past volumes
    min_avg_volume = np.percentile(historical_volumes, MIN_AVERAGE_PERCENTILE)  # 25%
    if avg_volume < min_avg_volume:
        return None, False  # Stock is too illiquid for confident spike detection
    
    percentile_volume = np.percentile(historical_volumes, VOLUME_PERCENTILE_THRESHOLD)  # 80%
    
    is_above_std_threshold  = latest_volume > avg_volume + STD_DEV_MULTIPLIER * std_volume
    is_above_percentile_threshold  = latest_volume > percentile_volume
    has_high_volume = is_above_std_threshold and is_above_percentile_threshold
    
    return latest_volume, has_high_volume

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

def has_increasing_volume(
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
        
        stock_name = stock.info.get('longName', ticker)

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

        latest_volume, has_high_volume = has_high_confidence_spike(hist)
        latest_price = hist['Close'].iloc[-1] if not hist.empty else None

        if not latest_volume or not has_high_volume:
            logger.debug(f"Invalid or insufficient volume data for {ticker}")
            return False, stock_name, latest_price, None

        if has_high_volume:
            logger.debug(f"{ticker}: has higher volume spike: {latest_volume} ")

        return has_high_volume, stock_name, latest_price, latest_volume

    except Exception as e:
        logger.warning(f"Error checking {ticker}: {e}")
        return False, ticker, None, None

def find_high_volume_stocks(max_workers: int = MAX_WORKERS) -> List[Tuple[str, str, Optional[float], Optional[int], bool]]:
    """Find stocks with volume surge based on moving average."""
    tickers = load_trending_tickers()
    results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(has_increasing_volume, ticker): ticker for ticker in tickers}
        for future in as_completed(futures):
            ticker = futures[future]
            try:
                high_vol, name, price, volume = future.result()
                if high_vol and volume:
                    results.append((ticker, name, price, volume, high_vol))
            except Exception as err:
                logger.warning(f"Error processing {ticker}: {err}")

    logger.info(f"Found {len(results)} high-volume stocks")
    return sorted(results, key=lambda x: x[0])

# --- Main Entry ---
if __name__ == "__main__":
    try:
        init_cache_db()
        logger.info("Starting high-volume stock screening...")
        tickers = find_high_volume_stocks()
        save_volume_tickers_to_db(tickers)
        logger.info(f"Completed. {len(tickers)} tickers updated in DB.")
    except Exception as main_err:
        logger.error(f"Fatal error: {main_err}")
        print(f"Error: {main_err}")
