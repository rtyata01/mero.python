import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_squared_error

def add_technical_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds features: price_to_vol, lagged price_to_vol, simple VWAP.
    Expects df to have columns: ['Open','High','Low','Close','Volume'].
    """
    df = df.copy()
    df["price_to_vol"] = df["Close"] / (df["Volume"] + 1e-6)

    # Compute VWAP cumulatively
    pv = (df["Close"] * df["Volume"]).cumsum()
    cvol = df["Volume"].cumsum()
    df["VWAP"] = pv / (cvol + 1e-6)

    # Example: rolling lags
    df["lag1_pv"] = df["price_to_vol"].shift(1)
    df["lag5_pv"] = df["price_to_vol"].shift(5)
    df["lag1_vwap"] = df["VWAP"].shift(1)
    df = df.dropna()
    return df

def train_and_evaluate(df: pd.DataFrame,
                       feature_cols: list,
                       target_col: str = "Close",
                       lookahead: int = 1) -> float:
    """
    Train a simple RandomForestRegressor to predict next-step return,
    report walk-forward validation RMSE.
    """
    df = df.copy()
    df["target"] = df[target_col].shift(-lookahead) / df[target_col] - 1.0
    df = df.dropna()

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
        rmses.append(mean_squared_error(y_val, pred, squared=False))

    return float(np.mean(rmses)), float(np.std(rmses))
