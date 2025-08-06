# Screen the high volume stocks
# has_high_volume = latest_volume > avg_volume * threshold (25%)

import time
import random
import logging
import backoff
import sqlite3
import pandas as pd
import yfinance as yf
from ftplib import FTP
from io import BytesIO
from csv import DictReader
from typing import List, Tuple, Optional
from contextlib import contextmanager
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
from screener_utils import init_cache_db, get_stock_history, save_stock_history

# --- Configuration ---
DATA_DIR = "data"
DB_NAME = "stock_data_cache.db"
MAX_WORKERS = 3
VOLUME_LOOKBACK_DAYS = 10
VOLUME_THRESHOLD = 1.25
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

def get_active_tickers() -> List[str]:
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
            return sorted(set(tickers))
    except Exception as e:
        msg = f"FTP connection failed: {e}"
        logger.error(msg)
        raise ConnectionError(msg)


def calculate_volume_stats(hist: pd.DataFrame) -> Tuple[Optional[int], Optional[float]]:
    """Calculate latest and average volume from history."""
    if hist.empty or len(hist) < 2:
        return None, None
    latest_volume = hist['Volume'].iloc[-1]
    avg_volume = hist['Volume'].iloc[:-1].mean()
    return int(latest_volume), avg_volume

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

def has_increasing_average_volume(
    ticker: str,
    lookback_days: int = VOLUME_LOOKBACK_DAYS,
    threshold: float = VOLUME_THRESHOLD
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

        latest_volume, avg_volume = calculate_volume_stats(hist)
        latest_price = hist['Close'].iloc[-1] if not hist.empty else None

        if not latest_volume or not avg_volume or avg_volume == 0:
            logger.debug(f"Invalid or insufficient volume data for {ticker}")
            return False, stock_name, latest_price, None

        has_high_volume = latest_volume > avg_volume * threshold

        if has_high_volume:
            logger.debug(f"{ticker}: {latest_volume} > {avg_volume * threshold:.0f} (avg × {threshold})")

        return has_high_volume, stock_name, latest_price, latest_volume

    except Exception as e:
        logger.warning(f"Error checking {ticker}: {e}")
        return False, ticker, None, None


def find_high_volume_stocks(max_workers: int = MAX_WORKERS) -> List[Tuple[str, str, Optional[float], Optional[int], bool]]:
    """Find stocks with volume surge based on moving average."""
    tickers = get_active_tickers()
    results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(has_increasing_average_volume, ticker): ticker for ticker in tickers}
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


def save_volume_tickers_to_db(ticker_data: List[Tuple[str, str, Optional[float], Optional[int], bool]]):
    """Insert or update high-volume tickers in DB."""
    try:
        with db_connection() as conn:
            inserted = 0
            for symbol, name, price, volume, rising in ticker_data:
                if rising:
                    conn.execute("""
                        INSERT OR REPLACE INTO eligible_stocks (symbol, stock_name, price, volume, has_rising_volume)
                        VALUES (?, ?, ?, ?, ?)
                    """, (symbol, name, price, volume, 1))
                    inserted += 1
            conn.commit()
            logger.info(f"{inserted} stocks saved to database")
    except Exception as e:
        logger.error(f"Database insert failed: {e}")
        raise RuntimeError("DB insert failed") from e


# --- Main Execution ---

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