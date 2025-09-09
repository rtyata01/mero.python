# Obtain recent stock data and computes short-term features (returns, volatility, momentum, and volume z-score) for each ticker.
# Compresses these features into lower-dimensional embeddings and builds a nearest-neighbor index for similarity search.
# Generate buy signal, if the latest price is below the 7-day average and the current embedding is similar to past patterns.
# Save all embeddings into a single CSV file.

import os
import logging
import yfinance as yf
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime, timedelta
from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors
from screener_utils import load_trending_tickers, get_stock_history

# -------------------- Configuration --------------------
DATE_FORMAT = "%Y%m%d"
DATA_DIR = "data"
LOOKBACK_DAYS = 90

# -------------------- Logging --------------------
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# ---------- 1. Download Stock Data ----------
def get_stock_data(ticker):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=LOOKBACK_DAYS + 1)
    df = get_stock_history(ticker, start_date, end_date) 
    df.dropna(inplace=True)
        
    # Ensure "Adj Close" column exists, otherwise use "Close"
    if "Adj Close" not in df.columns:
        df["Adj Close"] = df["Close"]

    return df

# ---------- 2. Short-term Features ----------
def add_short_term_features(df):
    df["returns"] = df["Adj Close"].pct_change()
    df["volatility"] = df["returns"].rolling(7).std()
    df["momentum"] = df["Adj Close"] / df["Adj Close"].rolling(7).mean()
    df["volume_z"] = (df["Volume"] - df["Volume"].rolling(7).mean()) / df["Volume"].rolling(7).std()
    df.dropna(inplace=True)
    return df

# ---------- 3. Generate Embeddings ----------
def make_embeddings(df, n_components=2):
    features = df[["returns", "volatility", "momentum", "volume_z"]].dropna().values
    if len(features) < n_components:
        return None
    pca = PCA(n_components=n_components)
    vectors = pca.fit_transform(features)
    return vectors

# ---------- 4. Build Vector Database ----------
def build_vector_db(vectors):
    nn = NearestNeighbors(n_neighbors=2, metric="euclidean")
    nn.fit(vectors)
    return nn

# ---------- 5. Simple Buy Signal ----------
def detect_buy_signals(df, nn, vectors):
    latest_vec = vectors[-1].reshape(1, -1)
    _, indices = nn.kneighbors(latest_vec)
    similar_dates = df.iloc[indices[0]].index

    # Example rule: Buy if price is below 7-day mean (short-term oversold)
    if df["Adj Close"].iloc[-1] < df["Adj Close"].rolling(7).mean().iloc[-1]:
        return f"BUY signal detected! Similar to {similar_dates.tolist()}"
    else:
        return "No buy signal."

# ---------- 6. Save all vectors into one CSV ----------
def save_vectors_csv(ticker, df, vectors):
    date_str = datetime.today().strftime(DATE_FORMAT)
    filename_with_date = f"vector_db_{date_str}.csv"
    file_name = os.path.join(Path(__file__).resolve().parent, DATA_DIR, filename_with_date)
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    
    # Ensure vectors is 2D numpy array
    vectors = np.array(vectors)
    
    # Create a simple DataFrame with proper column names
    col_names = [f"PC{i}" for i in range(vectors.shape[1])]
    vec_df = pd.DataFrame(vectors, index=df.index[-len(vectors):], columns=col_names)
    
    vec_df.reset_index(inplace=True)
    vec_df.rename(columns={"index": "date"}, inplace=True)
    vec_df.insert(0, "ticker", ticker)

    # Append to one big CSV
    try:
        existing = pd.read_csv(file_name)
        combined = pd.concat([existing, vec_df], ignore_index=True)
    except FileNotFoundError:
        combined = vec_df

    combined.to_csv(file_name, index=False)

# ---------- MAIN ----------
if __name__ == "__main__":
    tickers_to_screen = load_trending_tickers()
    for ticker in tickers_to_screen:
        logger.info(f"Processing stock -> {ticker}")
        df = get_stock_data(ticker)
        df = add_short_term_features(df)

        vectors = make_embeddings(df)
        if vectors is None:
            logger.info(f"{ticker} -> Not enough data for PCA")
        else:
            nn = build_vector_db(vectors)  # nearest neighbors model
            signal = detect_buy_signals(df, nn, vectors)
            logger.info(f"{ticker} -> {signal}")
            # save_vectors_csv(ticker, df, vectors)

        