# Based on the historic price and volume, add tecnical features
    # Momentum indicators (RSI, MACD).
    # Trend indicators (SMA, EMA).
    # Volatility & risk features (ATR, Bollinger bands, std dev).
    # Market sentiment proxy (fear_greed)
# Train the mode, using RandomForestRegressor for short term and GradientBoostingRegressor for long term.
# Split into train/test (80/20) and Predict short term buy/sale/hold decisions.

import time
import random
import logging
import backoff
import sqlite3
import pandas as pd
import numpy as np
import yfinance as yf
import ta
import warnings
from collections import defaultdict
from pathlib import Path
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Generator, Optional, Tuple, List
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split, TimeSeriesSplit
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from contextlib import contextmanager
from screener_utils import init_cache_db, get_stock_history, save_stock_history, load_quality_tickers, DEFAULT_TRENDING_STOCKS
warnings.filterwarnings('ignore')

# -------------------- Configuration -------------------- #

DATA_DIR = "data"
DB_NAME = "stock_data_cache.db"
DB_PATH = Path(__file__).resolve().parent / DATA_DIR / DB_NAME
MAX_WORKERS = 5
DATE_FORMAT = "%Y-%m-%d"
LOOKBACK_DAYS = 90
SHORT_TERM_DAYS = 5
LONG_TERM_DAYS = 30

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

def load_quality_tickers() -> List[str]:
    try:
        with db_connection() as conn:
            query = "SELECT symbol FROM eligible_stocks WHERE CAST(quality_score AS INTEGER) >= 4"
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
    
# -------------------- Machine Learning Functions -------------------- #

def add_technical_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Adds technical indicators """
    try:
        if not all(col in df.columns for col in ['Close', 'Volume']):
            logger.warning(f"Missing required columns in DataFrame: {df.columns}")
            return pd.DataFrame()
        df = df.copy()
    
        # Price-based features
        df['price_change'] = df['Close'].pct_change()
        df['price_change_5d'] = df['Close'].pct_change(5)
        df['price_change_10d'] = df['Close'].pct_change(10)
        
        # Moving averages
        df['sma_5'] = ta.trend.sma_indicator(df['Close'], window=5)
        df['sma_10'] = ta.trend.sma_indicator(df['Close'], window=10)
        df['sma_20'] = ta.trend.sma_indicator(df['Close'], window=20)
        df['sma_50'] = ta.trend.sma_indicator(df['Close'], window=50)
        
        # Exponential moving averages
        df['ema_12'] = ta.trend.ema_indicator(df['Close'], window=12)
        df['ema_26'] = ta.trend.ema_indicator(df['Close'], window=26)
        
        # RSI (Relative Strength Index)
        df['rsi'] = ta.momentum.rsi(df['Close'], window=14)
        
        # MACD
        df['macd'] = ta.trend.macd_diff(df['Close'])
        df['macd_signal'] = ta.trend.macd_signal(df['Close'])
        
        # Bollinger Bands
        bb_indicator = ta.volatility.BollingerBands(df['Close'])
        df['bb_upper'] = bb_indicator.bollinger_hband()
        df['bb_lower'] = bb_indicator.bollinger_lband()
        df['bb_position'] = (df['Close'] - df['bb_lower']) / (df['bb_upper'] - df['bb_lower'])
        
        # Volume indicators
        df['volume_change'] = df['Volume'].pct_change()
        df['volume_sma'] = df['Volume'].rolling(window=20).mean()
        
        # Volatility
        df['volatility'] = df['Close'].rolling(window=20).std()
        
        # Support and resistance levels
        df['high_20d'] = df['Close'].rolling(window=20).max()
        df['low_20d'] = df['Close'].rolling(window=20).min()
        df['price_position'] = (df['Close'] - df['low_20d']) / (df['high_20d'] - df['low_20d'])
        
        # Market sentiment indicatorscls
        df['fear_greed'] = (df['Close'] - df['sma_20']) / df['volatility']
    
        df = df.dropna()
        return df
    except Exception as e:
        logger.warning(f"Error in add_technical_indicators: {str(e)}")
        return pd.DataFrame()

def add_technical_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add feature matrix for machine learning"""
        
    feature_columns = [
        'price_change', 'price_change_5d', 'price_change_10d',
        'sma_5', 'sma_10', 'sma_20', 'sma_50',
        'ema_12', 'ema_26', 'rsi', 'macd', 'macd_signal',
        'bb_position', 'volume_change', 'volume_sma',
        'volatility', 'price_position', 'fear_greed'
    ]
    
    # Normalize features relative to current price
    df = df.copy()
    for col in ['sma_5', 'sma_10', 'sma_20', 'sma_50', 'ema_12', 'ema_26']:
        df[col] = df[col] / df['Close']
    
    df['volatility'] = df['volatility'] / df['Close']
    
    features = df[feature_columns].fillna(method='ffill').fillna(0)
    return features
        
def add_technical_targets(df: pd.DataFrame) -> pd.DataFrame:
    """Create target variables for short and long term predictions"""
    df = df.copy()
    
    # Short-term target: price change over next N days
    df['short_target'] = df['Close'].shift(-SHORT_TERM_DAYS) / df['Close'] - 1
    
    # Long-term target: price change over next N days
    df['long_target'] = df['Close'].shift(-LONG_TERM_DAYS) / df['Close'] - 1
    
    targets = df[['short_target', 'long_target']].fillna(0)
    return targets

def train_prediction_models(features: pd.DataFrame, targets: pd.DataFrame) -> defaultdict:
    """Train separate models for short and long term predictions"""
    if targets is None or features is None:
        print("Skipping! Targets and Features must not be empty.")
        return None
    
    # Remove rows where we don't have future data
    valid_idx = ~(targets['short_target'] == 0) & ~(targets['long_target'] == 0)
    X = features[valid_idx]
    y_short = targets['short_target'][valid_idx]
    y_long = targets['long_target'][valid_idx]
    
    if len(X) < 50:
        print("Not enough data for training. Need at least 30 valid samples.")
        return None
    
    # Split data
    X_train, X_test, y_short_train, y_short_test, y_long_train, y_long_test = train_test_split(
        X, y_short, y_long, test_size=0.2, random_state=42, shuffle=False
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train short-term model
    short_model = GradientBoostingRegressor(
        n_estimators=100, learning_rate=0.1, max_depth=6, random_state=42
    )
    short_model.fit(X_train_scaled, y_short_train)
    
    # Train long-term model
    long_model = RandomForestRegressor(
        n_estimators=100, max_depth=8, random_state=42
    )
    long_model.fit(X_train_scaled, y_long_train)
    
    # Evaluate models
    short_pred = short_model.predict(X_test_scaled)
    long_pred = long_model.predict(X_test_scaled)
    
        # Calculate metrics
    short_r2 = r2_score(y_short_test, short_pred)
    short_rmse = np.sqrt(mean_squared_error(y_short_test, short_pred))
    long_r2 = r2_score(y_long_test, long_pred)
    long_rmse = np.sqrt(mean_squared_error(y_long_test, long_pred))
    
    print("Model Performance:")
    print(f"Short-term R² Score: {short_r2:.4f}")
    print(f"Short-term RMSE: {short_rmse:.4f}")
    print(f"Long-term R² Score: {long_r2:.4f}")
    print(f"Long-term RMSE: {long_rmse:.4f}")
    
    return {
        'short_model': short_model,
        'long_model': long_model,
        'scaler': scaler,
        'performance': {
            'short_r2': short_r2,
            'short_rmse': short_rmse,
            'long_r2': long_r2,
            'long_rmse': long_rmse
        },
        'feature_names': X.columns.tolist()
    }
        
def make_predictions(df: pd.DataFrame, md: defaultdict=None) -> defaultdict:
    """Make predictions for the next period"""
    if md is None:
        print("Models not trained yet.")
        return None
    
    # Recreate features from the enhanced dataframe
    features = add_technical_features(df)

    # Get latest features
    latest_features = features.iloc[-1:].values
    latest_scaled = md['scaler'].transform(latest_features)
    
    # Make predictions
    short_pred = md['short_model'].predict(latest_scaled)[0]
    long_pred = md['long_model'].predict(latest_scaled)[0]
    
    current_price = df['Close'].iloc[-1]
    
    # Calculate confidence scores
    recent_volatility = df['volatility'].iloc[-20:].mean() / current_price
    short_confidence = max(0.7 - min(recent_volatility * 10, 0.3) - min(abs(short_pred) * 2, 0.2), 0.1)
    long_confidence = max(0.7 - min(recent_volatility * 10, 0.3) - min(abs(long_pred) * 2, 0.2), 0.1)
    
    return {
        'current_price': current_price,
        'short_term': {
            'predicted_change': short_pred,
            'predicted_price': current_price * (1 + short_pred),
            'confidence': short_confidence,
            'timeframe': f'{SHORT_TERM_DAYS} days'
        },
        'long_term': {
            'predicted_change': long_pred,
            'predicted_price': current_price * (1 + long_pred),
            'confidence': long_confidence,
            'timeframe': f'{LONG_TERM_DAYS} days'
        }
    }
    
def make_recommendation(predictions: defaultdict = None):
    """Generate trading recommendation based on predictions"""
    if predictions is None:
        return None, None
    
    short_change = predictions['short_term']['predicted_change']
    long_change = predictions['long_term']['predicted_change']
    short_conf = predictions['short_term']['confidence']
    long_conf = predictions['long_term']['confidence']
    
    # Thresholds for decision making
    strong_threshold = 0.05  # 5% change
    moderate_threshold = 0.02  # 2% change
    
    st_forcast = ""
    lt_forcast = ""
    
    if short_change > strong_threshold and short_conf > 0.6:
        st_forcast += "STRONG BUY"
    elif short_change > moderate_threshold and short_conf > 0.5:
        st_forcast += "BUY"
    elif short_change < -strong_threshold and short_conf > 0.6:
        st_forcast += "STRONG"
    elif short_change < -moderate_threshold and short_conf > 0.5:
        st_forcast += "SELL"
    else:
        st_forcast += "HOLD"
    
    if long_change > strong_threshold and long_conf > 0.6:
        lt_forcast += "STRONG BUY"
    elif long_change > moderate_threshold and long_conf > 0.5:
        lt_forcast += "BUY"
    elif long_change < -strong_threshold and long_conf > 0.6:
        lt_forcast += "STRONG SELL"
    elif long_change < -moderate_threshold and long_conf > 0.5:
        lt_forcast += "SELL"
    else:
        lt_forcast += "HOLD"
    
    return st_forcast, lt_forcast

def predict_signal_recommendation(ticker: str, hist: pd.DataFrame) -> float:
    """Predict next-day return and compute a normalized score (0-1)."""
    try:
        logger.info(f"Predicting (buy/sell/hold) signal for {ticker}")

        if hist.empty or len(hist) < 30:
            logger.warning(f"Insufficient history for {ticker} to predict return")
            return None

        # Add technical indicators
        df_enhanced  = add_technical_indicators(hist)
        features = add_technical_features(df_enhanced)
        targets = add_technical_targets(df_enhanced)
        
        # Train final model and predict next-day return
        models = train_prediction_models(features, targets)
        if models is None:
            logger.warning(f"Skipping! No trained models created.")
            return None

        # Make Predictions
        predictions = make_predictions(df_enhanced, models)
        if predictions is None:
            logger.warning(f"Skipping! No predictions created.")
            return None
        
        # Make recommendation
        short_term_signal, _ = make_recommendation(predictions)

        return short_term_signal
    
    except Exception as e:
        logger.warning(f"Error predicting (buy/sell/hold) signal for {ticker}: {str(e)}")
        return None

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

def predict_stock_signals(
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
        
        # Predicted signal
        predicted_signal = predict_signal_recommendation(ticker, hist)
        
        return predicted_signal, stock_name, latest_price, latest_volume

    except Exception as e:
        logger.warning(f"Error checking {ticker}: {e}")
        return False, ticker, None, None

def train_predict_stock_signals(max_workers: int = MAX_WORKERS, monthly_screen: bool = False) -> List[Tuple[str, str, Optional[float], Optional[int], bool]]:
    """Find stocks with better quality."""
    tickers_to_screen = load_quality_tickers()
    results = []
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(predict_stock_signals, ticker): ticker for ticker in tickers_to_screen}
        for future in as_completed(futures):
            ticker = futures[future]
            try:
                predicted_signal, name, price, volume = future.result()
                if predicted_signal:
                    results.append((ticker, name, price, volume, predicted_signal))
            except Exception as err:
                logger.warning(f"Error processing {ticker}: {err}")

    logger.info(f"Found {len(results)} predicted high quality stocks.")
    return sorted(results, key=lambda x: x[0])

def save_predicted_signals_to_db(ticker_data: List[Tuple[str, str, Optional[float], Optional[int], bool]]):
    """Insert or update high-volume tickers in DB."""
    try:
        with db_connection() as conn:
            cursor = conn.cursor()
        
            # Reset the predicted_signal field for all stocks
            cursor.execute("UPDATE eligible_stocks SET predicted_signal = NULL")
            
            # Prepare data for bulk insert (only those with rising volume)
            data_to_insert = [
                (symbol, name, price, volume, signal)
                for symbol, name, price, volume, signal in ticker_data
            ]
            
            if data_to_insert:
                # Bulk insert using executemany
                cursor.executemany("""
                    INSERT OR REPLACE INTO eligible_stocks (symbol, stock_name, price, volume, predicted_signal)
                    VALUES (?, ?, ?, ?, ?)
                """, data_to_insert)
                
                # Commit all changes in one transaction
                conn.commit()
                logger.info(f"{len(data_to_insert)} stocks with predicted stock signals saved to database.")
            else:
                logger.info("No stocks with predicted stock signals to insert.")
    except Exception as e:
        logger.error(f"Database insert failed: {e}")
        raise RuntimeError("DB insert failed") from e

# --- Main Execution ---
if __name__ == "__main__":
    try:
        init_cache_db()
        logger.info("Screening for predicted stocks signal ...")
        tickers = train_predict_stock_signals()
        save_predicted_signals_to_db(tickers)
        logger.info(f"Found {len(tickers)} predicted stocks signal.")
    except Exception as main_err:
        logger.error(f"Fatal error: {main_err}")
        print(f"Error: {main_err}")