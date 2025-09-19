import logging
import sqlite3
import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta
from ftplib import FTP
from contextlib import contextmanager
from typing import List, Generator

# -------------------- Configuration -------------------- #

DATA_DIR = "data"
DB_NAME = "stock_data_cache.db"
DB_PATH = Path(__file__).resolve().parent / DATA_DIR / DB_NAME

MAX_WORKERS = 10
MAINTAIN_WEEKS_BACK = 26  # Store last six months data (2 * 26 = 52 weeks) (1 Year)
DATE_FORMAT = "%Y-%m-%d"
DEFAULT_TRENDING_STOCKS = ["NIO","TSLA","NVDA","AMD","PLTR", "SOFI", "SMCI", "MSFT", "GOOGL", "AMZN", "AAPL"]

# -------------------- Logging Setup -------------------- #

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# -------------------- Context Managers -------------------- #

@contextmanager
def ftp_connection(host: str) -> Generator[FTP, None, None]:
    ftp = FTP(host)
    try:
        ftp.login()
        yield ftp
    finally:
        ftp.quit()

@contextmanager
def db_connection() -> Generator[sqlite3.Connection, None, None]:
    """Context manager for SQLite DB connection."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()

# -------------------- Database Initialization -------------------- #

def init_cache_db() -> None:
    """Create required tables in the cache database."""
    with db_connection() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS stock_history (
                ticker TEXT,
                date TEXT,
                price REAL,
                volume INTEGER,
                PRIMARY KEY (ticker, date)
            );
            
            CREATE TABLE IF NOT EXISTS eligible_stocks (
                symbol TEXT PRIMARY KEY,
                stock_name TEXT,
                price REAL,
                volume INTEGER,
                has_rising_volume BOOLEAN,
                has_rising_price BOOLEAN,
                fundamental_score INTEGER,
                quality_score INTEGER,
                predicted_quality_score INTEGER,
                predicted_signal TEXT
            );
        """)
        # conn.execute("ALTER TABLE eligible_stocks ADD COLUMN fundamental_score INTEGER DEFAULT 0;")
        # conn.execute("ALTER TABLE eligible_stocks ADD COLUMN quality_score INTEGER DEFAULT 0;")
        # conn.execute("ALTER TABLE eligible_stocks ADD COLUMN predicted_quality_score INTEGER DEFAULT 0;")
        # conn.execute("ALTER TABLE eligible_stocks ADD COLUMN predicted_signal TEXT;")
        conn.commit()
    logger.info("Database initialized with required tables.")
    

# -------------------- Stock Data Retrieval -------------------- #

def get_stock_history(ticker: str, start_date: datetime, end_date: datetime) -> pd.DataFrame:
    """Retrieve cached stock data from the database."""
    with db_connection() as conn:
        query = """
            SELECT date, price, volume 
            FROM stock_history
            WHERE ticker = ? AND date BETWEEN ? AND ?
            ORDER BY date
        """
        df = pd.read_sql_query(
            query,
            conn,
            params=(ticker, start_date.strftime(DATE_FORMAT), end_date.strftime(DATE_FORMAT)),
            parse_dates=['date']
        )

    if df.empty:
        # logger.info(f"No cached data found for {ticker} between {start_date} and {end_date}.")
        return pd.DataFrame()

    return (
        df.rename(columns={'date': 'Date', 'price': 'Close', 'volume': 'Volume'})
          .set_index('Date')
    )

# -------------------- Stock Data Saving -------------------- #

def save_stock_history(ticker: str, df: pd.DataFrame) -> None:
    """Save stock data to the cache and clean outdated records."""
    if df.empty:
        logger.warning(f"No data to save for {ticker}.")
        return

    with db_connection() as conn:
        df = (
            df.reset_index()
              .assign(
                  ticker=ticker,
                  date=lambda d: d['Date'].dt.strftime(DATE_FORMAT),
                  price=lambda d: d['Close'].astype(float),
                  volume=lambda d: d['Volume'].astype(int)
              )
        )

        cached_dates = pd.read_sql_query(
            "SELECT date FROM stock_history WHERE ticker = ?",
            conn,
            params=(ticker,)
        )['date'].tolist()

        new_data = df[~df['date'].isin(cached_dates)]

        if new_data.empty:
            logger.info(f"No new data to cache for {ticker}.")
        else:
            new_data[['ticker', 'date', 'price', 'volume']].to_sql(
                'stock_history',
                conn,
                if_exists='append',
                index=False,
                method='multi'
            )
            logger.info(f"Cached {len(new_data)} new records for {ticker}.")

        # Cleanup old records
        cutoff_date = (datetime.now() - timedelta(weeks=MAINTAIN_WEEKS_BACK)).strftime(DATE_FORMAT)
        deleted = conn.execute(
            "DELETE FROM stock_history WHERE date < ?", (cutoff_date,)
        ).rowcount
        conn.commit()

        if deleted:
            logger.info(f"Deleted {deleted} outdated records from cache for {ticker}.")

# --- Helper Functions ---

def load_trending_tickers() -> List[str]:
    try:
        with db_connection() as conn:
            query = "SELECT symbol FROM eligible_stocks WHERE CAST(fundamental_score AS INTEGER) >= 7"
            df = pd.read_sql_query(query, conn)
            if df.empty:
                logger.warning("No trending tickers found.")
                return []
            tickers = df["symbol"].dropna().str.upper().str.strip().unique().tolist()
            
            # Append the default trending stocks
            tickers.extend(DEFAULT_TRENDING_STOCKS)
            logger.info(f"Loaded {len(tickers)} trending tickers.")
            
            return sorted(tickers)
    except Exception as e:
        logger.error(f"Error loading tickers: {e}")
        raise


def load_quality_tickers() -> List[str]:
    try:
        with db_connection() as conn:
            query = "SELECT symbol FROM eligible_stocks WHERE CAST(quality_score AS INTEGER) >= 7"
            df = pd.read_sql_query(query, conn)
            if df.empty:
                logger.warning("No quality tickers found.")
                return []
            tickers = df["symbol"].dropna().str.upper().str.strip().unique().tolist()
            
            # Append the default trending stocks
            tickers.extend(DEFAULT_TRENDING_STOCKS)
            logger.info(f"Loaded {len(tickers)} quality tickers.")
            
            return sorted(tickers)
    except Exception as e:
        logger.error(f"Error loading tickers: {e}")
        raise