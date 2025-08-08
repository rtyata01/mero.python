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
MAX_WORKERS = 5
LOOKBACK_DAYS = 60
VOLUME_PERCENTILE_THRESHOLD = 80.0    # e.g. today's volume must exceed the 80th percentile
MIN_AVERAGE_PERCENTILE = 25.0         # e.g. filter out lowest 25% volume days dynamically
STD_DEV_MULTIPLIER = 2.0              # require volume > mean + 2·std_dev
DATE_FORMAT = "%Y-%m-%d"
DEFAULT_TRENDING_STOCKS = ["NIO","TSLA","NVDA","AMD","PLTR", "SOFI", "SMCI", "MSFT", "GOOGL", "AMZN", "AAPL"]

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
            
            # Append the default trending stocks
            tickers.extend(DEFAULT_TRENDING_STOCKS)
            return sorted(set(tickers))
    except Exception as e:
        msg = f"FTP connection failed: {e}"
        logger.error(msg)
        raise ConnectionError(msg)


def has_incrementing_monthly_prices(hist):
    """Check if monthly average prices are increasing."""
    if not isinstance(hist, pd.DataFrame) or hist.empty:
        return False
    try:
        monthly_prices = hist['Close'].resample('ME').mean()
        prices = monthly_prices.values
        return all(prices[i] < prices[i + 1] for i in range(len(prices) - 1))
    except Exception:
        return False

def has_high_volume_trend(hist):
    """Check if trading volume is increasing or high."""
    if not isinstance(hist, pd.DataFrame) or hist.empty or hist['Volume'].isnull().all():
        return False
    try:
        weekly_volume = hist['Volume'].resample('W').mean()
        avg_volume = weekly_volume.mean()
        recent_volume = weekly_volume[-4:].mean()
        return recent_volume > avg_volume * 1.2
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
    """Predict fundamental score greater than 4 out of 6, will be likely good"""
    score = 0
    industry_avg_roe = 0.15
    industry_avg_debt_to_equity = 1.0
    industry_avg_pe = 25

    eps = stock.info.get("trailingEps", None)
    if isinstance(eps, (int, float)) and eps > 0:
        score += 1

    roe = stock.info.get("returnOnEquity", None)
    if isinstance(roe, (int, float)) and roe > industry_avg_roe:
        score += 1

    debt_to_equity = stock.info.get("debtToEquity", None)
    if isinstance(debt_to_equity, (int, float)) and (debt_to_equity * 0.01) < industry_avg_debt_to_equity:
        score += 1

    pe_ratio = stock.info.get("trailingPE", None)
    if isinstance(pe_ratio, (int, float)) and pe_ratio < industry_avg_pe:
        score += 1

    if has_incrementing_monthly_prices(hist):
        score += 1

    if has_high_volume_trend(hist):
        score += 1

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


def find_trending_stocks(tickers = None, max_workers: int = MAX_WORKERS) -> List[Tuple[str, str, Optional[float], Optional[int], bool]]:
    """Find stocks with volume surge based on moving average."""
    tickers = tickers if tickers else get_active_tickers()
    results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(get_trending_stocks, ticker): ticker for ticker in tickers}
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
        tickers = find_trending_stocks(tickers=DEFAULT_TRENDING_STOCKS)
        save_trending_tickers_to_db(tickers)
        logger.info(f"Found {len(tickers)} trending stocks.")
    except Exception as main_err:
        logger.error(f"Fatal error: {main_err}")
        print(f"Error: {main_err}")