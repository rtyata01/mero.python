# Screen the high volume stocks and find stock with higher average monthly price for last 12 Weeks i.e. ~3 months.
# latest price > price 12 weeks before
# is_increasing_percent = count consecutive price increments (day[i] > day[i-1]) / total number of days > 0.75 
# Noisy signal = 50%  
# Balanced signal = 66.67%
# High signal = 75%

import time
import random
import logging
import backoff
import sqlite3
import pandas as pd
import yfinance as yf
from pathlib import Path
from datetime import datetime, timedelta
from contextlib import contextmanager
from typing import List, Tuple, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from screener_utils import init_cache_db, get_stock_history, save_stock_history, load_trending_tickers, DEFAULT_TRENDING_STOCKS

# --- Configuration ---
DATA_DIR = "data"
DB_NAME = "stock_data_cache.db"
MAX_WORKERS = 5
LOOKBACK_DAYS = 90
HIGH_CONFIDENCE_PERCENT = 0.75

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
def save_price_tickers_to_db(tickers_data: List[Tuple[str, str, float, int, bool]]):
    try:
        with db_connection() as conn:
            cursor = conn.cursor()
            
             # Reset the has_rising_volume field for all stocks
            cursor.execute("UPDATE eligible_stocks SET has_rising_price = CAST(0 AS INTEGER)")
            
             # Prepare data for batch update (only symbols with rising prices)
            updates = [(1, symbol) for symbol, _, _, _, is_rising in tickers_data if is_rising]

            if updates:
                cursor.executemany("""
                    UPDATE eligible_stocks
                    SET has_rising_price = ?
                    WHERE symbol = ?
                """, updates)
                
                conn.commit()
                logger.info(f"Updated {len(updates)} tickers with rising prices.")
            else:
                logger.info("No tickers with rising prices to update.")
    except Exception as e:
        logger.error(f"Error saving tickers: {e}")
        raise

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

# --- Monthly Price Checker ---
def has_increasing_monthly_prices(ticker: str) -> Tuple[bool, str, Optional[float], Optional[int]]:
    try:
        end = datetime.now()
        start = end - timedelta(days=LOOKBACK_DAYS)
        hist = get_stock_history(ticker, start, end)
        
        stock = yf.Ticker(ticker)
        sleep_with_jitter()  # Delay after each API cal
        stock_name = stock.info.get("longName", ticker)

        # Refresh cache if needed
        if hist.empty or hist.index.max().date() < (end - timedelta(days=1)).date():
            try:
                new_data = safe_fetch_stock_data(stock, start, end)
                if not new_data.empty:
                    save_stock_history(ticker, new_data)
                    hist = get_stock_history(ticker, start, end)
                sleep_with_jitter() # Delay after each API call
            except Exception as e:
                logger.debug(f"{ticker} fetch failed: {e}")
                return False, stock_name, None, None

        if hist.empty or len(hist) < int(LOOKBACK_DAYS * 0.6): # considering 70% trading days per week.
            logger.info(f"{ticker} do not have sufficient historic data and its below {LOOKBACK_DAYS * 0.6} days!")
            return False, stock_name, None, None

        # Ensure we're working with the 'Close' prices
        close_prices = hist['Close'].dropna()
        if close_prices.empty:
            logger.info(f"{ticker} is missing the latest price!")
            return False, stock_name, None, None

        # Compare start vs end price
        start_price = close_prices.iloc[0]
        latest_price = close_prices.iloc[-1]
        latest_volume = hist['Volume'].iloc[-1] if 'Volume' in hist else None

        if latest_price <= start_price:
            logger.info(f"{ticker} latest price: {latest_price} is lower than starting price {start_price}!")
            return False, stock_name, latest_price, latest_volume

        # Count daily increases
        daily_increases = sum(
            1 for i in range(1, len(close_prices)) if close_prices.iloc[i] > close_prices.iloc[i - 1]
        )

        percent_increase_days = daily_increases / (len(close_prices) - 1)
        is_increasing = percent_increase_days > HIGH_CONFIDENCE_PERCENT

        if is_increasing:
            logger.info(f"{ticker} has increasing price!")
            return is_increasing, stock_name, latest_price, latest_volume
        else:
            return False, stock_name, latest_price, latest_volume

    except Exception as e:
        logger.warning(f"{ticker} processing error: {e}")
        return False, ticker, None, None

# --- Main Processing Function ---
def find_increasing_price_stocks() -> List[Tuple[str, str, float, int, bool]]:
    try:
        tickers = load_trending_tickers()
        results = []

        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = {executor.submit(has_increasing_monthly_prices, t): t for t in tickers}
            for future in as_completed(futures):
                try:
                    rising, name, price, volume = future.result()
                    if rising and price:
                        results.append((futures[future], name, price, volume, rising))
                except Exception as e:
                    logger.warning(f"Failed processing {futures[future]}: {e}")

        logger.info(f"Found {len(results)} tickers with increasing prices.")
        return sorted(results, key=lambda x: x[0])

    except Exception as e:
        logger.error(f"Failed to find rising price stocks: {e}")
        raise

# --- Main Entry ---
if __name__ == "__main__":
    try:
        init_cache_db()
        rising_stocks = find_increasing_price_stocks()
        save_price_tickers_to_db(rising_stocks)

        count = len(rising_stocks)
        symbols = [t[0] for t in rising_stocks]
        logger.info(f"Completed: {count} rising-price tickers found.")
        print(f"Tickers with rising-prices ({count}): {symbols}")

    except Exception as e:
        logger.error(f"Execution error: {e}")
        print(f"Error: {e}")
