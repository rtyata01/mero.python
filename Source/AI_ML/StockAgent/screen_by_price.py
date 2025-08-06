# Screen the high volume stocks and find stock with higher average monthly price for last 3 months.
#   is_increasing = all(monthly_averages[i] < monthly_averages[i + 1] for i in range(len(monthly_averages) - 1))
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
from screener_utils import init_cache_db, get_stock_history, save_stock_history

# --- Configuration ---
DATA_DIR = "data"
DB_NAME = "stock_data_cache.db"
MAX_WORKERS = 3
WEEKS_BACK = 8
WEEKS_PER_MONTH = 4
MONTHS = 3

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

# --- Load High Volume Tickers ---
def load_high_volume_tickers() -> List[str]:
    try:
        with db_connection() as conn:
            query = "SELECT symbol FROM eligible_stocks WHERE CAST(has_rising_volume AS INTEGER) = 1"
            df = pd.read_sql_query(query, conn)
            if df.empty:
                logger.warning("No high-volume tickers found.")
                return []
            tickers = df["symbol"].dropna().str.upper().str.strip().unique().tolist()
            logger.info(f"Loaded {len(tickers)} tickers with rising volume.")
            return sorted(tickers)
    except Exception as e:
        logger.error(f"Error loading tickers: {e}")
        raise

# --- Save Ticker Data ---
def save_increasing_price_tickers(tickers_data: List[Tuple[str, str, float, int, bool]]):
    try:
        with db_connection() as conn:
            cursor = conn.cursor()
            count = 0
            for symbol, name, price, volume, is_rising in tickers_data:
                if is_rising:
                    cursor.execute("""
                        UPDATE eligible_stocks
                        SET stock_name = ?, latest_price = ?, latest_volume = ?, has_rising_price = ?
                        WHERE symbol = ?
                    """, (name, price, volume, int(is_rising), symbol))
                    count += 1
            conn.commit()
            logger.info(f"Updated {count} tickers with rising prices.")
    except Exception as e:
        logger.error(f"Error saving tickers: {e}")
        raise

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

# --- Monthly Price Checker ---
def has_increasing_monthly_prices(ticker: str) -> Tuple[bool, str, Optional[float], Optional[int]]:
    try:
        end = datetime.now()
        start = end - timedelta(weeks=WEEKS_BACK)
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

        if hist.empty or len(hist) < WEEKS_BACK * 5:
            return False, stock_name, None, None

        # Weekly to monthly
        weekly = hist['Close'].resample('W-MON').mean()
        if len(weekly) < MONTHS * WEEKS_PER_MONTH:
            return False, stock_name, None, None

        monthly_averages = [
            weekly[-(i + 1) * WEEKS_PER_MONTH : -i * WEEKS_PER_MONTH if i > 0 else None].mean()
            for i in reversed(range(MONTHS))
        ]

        is_increasing = all(a < b for a, b in zip(monthly_averages, monthly_averages[1:]))
        latest_price = hist['Close'].iloc[-1]
        latest_volume = hist['Volume'].iloc[-1] if 'Volume' in hist else None

        return is_increasing, stock_name, latest_price, latest_volume

    except Exception as e:
        logger.warning(f"{ticker} processing error: {e}")
        return False, ticker, None, None

# --- Main Processing Function ---
def find_stocks_with_rising_prices() -> List[Tuple[str, str, float, int, bool]]:
    try:
        tickers = load_high_volume_tickers()
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
        rising_stocks = find_stocks_with_rising_prices()
        save_increasing_price_tickers(rising_stocks)

        count = len(rising_stocks)
        symbols = [t[0] for t in rising_stocks]
        logger.info(f"Completed: {count} rising-price tickers found.")
        print(f"Tickers with rising 3-month average prices ({count}): {symbols}")

    except Exception as e:
        logger.error(f"Execution error: {e}")
        print(f"Error: {e}")
