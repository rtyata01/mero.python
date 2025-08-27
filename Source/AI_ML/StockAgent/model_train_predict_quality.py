# Performs time-series cross-validation with RandomForestRegressor.
# Predict and forecast the next-day percentage return (e.g., (next_day_close / current_close) - 1) 
# Based on technical features like price-to-volume, VWAP, and lagged features derrived from historic stock daily price and volume.
    # score = 0 indicates the predicted return is at the lower end of historical returns (e.g., negative or low positive return).
    # score = 1 indicates the predicted return is at the upper end (e.g., high positive return).
    # score = 0.5 represents the median historical return.

import time
import random
import logging
import backoff
import sqlite3
import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta
import yfinance as yf
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Generator, Optional, Tuple, List
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_squared_error
from contextlib import contextmanager
from screener_utils import init_cache_db, get_stock_history, save_stock_history, load_quality_tickers, DEFAULT_TRENDING_STOCKS

# -------------------- Configuration -------------------- #

DATA_DIR = "data"
DB_NAME = "stock_data_cache.db"
DB_PATH = Path(__file__).resolve().parent / DATA_DIR / DB_NAME
MAX_WORKERS = 5
DATE_FORMAT = "%Y-%m-%d"
LOOKBACK_DAYS = 60

# -------------------- Logging Setup -------------------- #

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# -------------------- Context Managers -------------------- #

@contextmanager
def db_connection() -> Generator[sqlite3.Connection, None, None]:
    """Context manager for SQLite DB connection."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()
    
# -------------------- Machine Learning Functions -------------------- #

def add_technical_features(df: pd.DataFrame) -> pd.DataFrame:
    """Adds technical features: price_to_vol, lagged price_to_vol, VWAP."""
    try:
        if not all(col in df.columns for col in ['Close', 'Volume']):
            logger.warning(f"Missing required columns in DataFrame: {df.columns}")
            return pd.DataFrame()
        df = df.copy()
        df["price_to_vol"] = df["Close"] / (df["Volume"] + 1e-6)
        pv = (df["Close"] * df["Volume"]).cumsum()
        cvol = df["Volume"].cumsum()
        df["VWAP"] = pv / (cvol + 1e-6)
        df["lag1_pv"] = df["price_to_vol"].shift(1)
        df["lag5_pv"] = df["price_to_vol"].shift(5)
        df["lag1_vwap"] = df["VWAP"].shift(1)
        df = df.dropna()
        return df
    except Exception as e:
        logger.warning(f"Error in add_technical_features: {str(e)}")
        return pd.DataFrame()


def train_and_evaluate(df: pd.DataFrame,
                       feature_cols: list,
                       target_col: str = "Close",
                       lookahead: int = 1) -> Tuple[float, float]:
    """Train a RandomForestRegressor and report walk-forward RMSE."""
    df = df.copy()
    df["target"] = df[target_col].shift(-lookahead) / df[target_col] - 1.0
    df = df.dropna()
    
    if df.empty:
        return None, None

    X = df[feature_cols].values
    y = df["target"].values

    tscv = TimeSeriesSplit(n_splits=5)
    rmses = []

    for train_idx, test_idx in tscv.split(X):
        X_tr, X_val = X[train_idx], X[test_idx]
        y_tr, y_val = y[train_idx], y[test_idx]
        mdl = RandomForestRegressor(n_estimators=100, max_depth=5, random_state=0, n_jobs=-1)
        mdl.fit(X_tr, y_tr)
        pred = mdl.predict(X_val)
        mse = mean_squared_error(y_val, pred)
        rmses.append(np.sqrt(mse))

    return float(np.mean(rmses)), float(np.std(rmses))

def predict_quality_score(ticker: str, hist: pd.DataFrame) -> float:
    """Predict next-day return and compute a normalized score (0-1)."""
    try:
        logger.info(f"Predicting quality score for {ticker}")

        if hist.empty or len(hist) < 30:
            logger.warning(f"Insufficient history for {ticker} to predict return")
            return 0.0

        # Add technical features
        df = add_technical_features(hist)
        if df.empty:
            return 0.0

        feature_cols = ["price_to_vol", "VWAP", "lag1_pv", "lag5_pv", "lag1_vwap"]

        # Ensure target column exists
        if "target" not in df.columns:
            df["target"] = df["Close"].shift(-1) / df["Close"] - 1.0
        df = df.dropna(subset=["target"])
        if df.empty:
            logger.warning(f"No valid rows for {ticker} after creating target")
            return 0.0

        # Train model and get RMSE
        rmse, _ = train_and_evaluate(df, feature_cols, target_col="Close", lookahead=1)
        if rmse is None:
            return 0.0

        # Train final model and predict next-day return
        X = df[feature_cols].values
        y = df["target"].values
        mdl = RandomForestRegressor(n_estimators=100, max_depth=5, random_state=0, n_jobs=-1)
        mdl.fit(X[:-1], y[:-1])
        predicted_return = mdl.predict(X[-1:])[0]

        # Normalize predicted return to 0-1 score
        hist_returns = df["target"]
        return_range = hist_returns.max() - hist_returns.min()
        if return_range == 0:
            normalized_score = 0.5
        else:
            normalized_score = (predicted_return - hist_returns.min()) / return_range
            normalized_score = np.clip(normalized_score, 0.0, 1.0)

        logger.info(f"Predicted quality score for {ticker}: {normalized_score:.2f}")
        return normalized_score

    except Exception as e:
        logger.warning(f"Error predicting quality score for {ticker}: {str(e)}")
        return 0.0

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

def predict_quality_stocks(
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
        
        # Predicted return score
        predicted_quality_score = predict_quality_score(ticker, hist)
        
        return predicted_quality_score, stock_name, latest_price, latest_volume

    except Exception as e:
        logger.warning(f"Error checking {ticker}: {e}")
        return False, ticker, None, None

def train_predict_quality_stocks(max_workers: int = MAX_WORKERS, monthly_screen: bool = False) -> List[Tuple[str, str, Optional[float], Optional[int], bool]]:
    """Find stocks with better quality."""
    tickers_to_screen = load_quality_tickers()
    results = []
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(predict_quality_stocks, ticker): ticker for ticker in tickers_to_screen}
        for future in as_completed(futures):
            ticker = futures[future]
            try:
                predicted_score, name, price, volume = future.result()
                if predicted_score == 1.0:
                    results.append((ticker, name, price, volume, predicted_score))
            except Exception as err:
                logger.warning(f"Error processing {ticker}: {err}")

    logger.info(f"Found {len(results)} predicted high quality stocks.")
    return sorted(results, key=lambda x: x[0])

def save_predicted_tickers_to_db(ticker_data: List[Tuple[str, str, Optional[float], Optional[int], bool]]):
    """Insert or update high-volume tickers in DB."""
    try:
        with db_connection() as conn:
            cursor = conn.cursor()
        
            # Reset the has_rising_volume field for all stocks
            cursor.execute("UPDATE eligible_stocks SET predicted_quality_score = CAST(0 AS INTEGER)")
            
            # Prepare data for bulk insert (only those with rising volume)
            data_to_insert = [
                (symbol, name, price, volume, score)
                for symbol, name, price, volume, score in ticker_data
            ]
            
            if data_to_insert:
                # Bulk insert using executemany
                cursor.executemany("""
                    INSERT OR REPLACE INTO eligible_stocks (symbol, stock_name, price, volume, predicted_quality_score)
                    VALUES (?, ?, ?, ?, ?)
                """, data_to_insert)
                
                # Commit all changes in one transaction
                conn.commit()
                logger.info(f"{len(data_to_insert)} stocks with predicted quality stocks saved to database.")
            else:
                logger.info("No stocks with predicted quality to insert.")
    except Exception as e:
        logger.error(f"Database insert failed: {e}")
        raise RuntimeError("DB insert failed") from e

# --- Main Execution ---
if __name__ == "__main__":
    try:
        init_cache_db()
        logger.info("Screening for predicted quality score...")
        tickers = train_predict_quality_stocks()
        save_predicted_tickers_to_db(tickers)
        logger.info(f"Found {len(tickers)} predicted quality stocks.")
    except Exception as main_err:
        logger.error(f"Fatal error: {main_err}")
        print(f"Error: {main_err}")