import os
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

def download_symbol_data(symbol: str,
                         start_date: pd.Timestamp,
                         end_date: pd.Timestamp,
                         interval: str = "1d",
                         auto_adjust: bool = True,
                         multi_index: bool = False) -> pd.DataFrame:
    """
    Download historical data for a symbol using yfinance.
    """
    df = yf.download(
        tickers=symbol,
        start=start_date.strftime("%Y-%m-%d"),
        end=(end_date + timedelta(days=1)).strftime("%Y-%m-%d"),
        interval=interval,
        auto_adjust=auto_adjust,
        threads=True,
        progress=False,
        multi_index=multi_index,
    )
    # If multi_index=True, flatten:
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.droplevel(1)
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    return df

def load_local_csv(file_path: str) -> pd.DataFrame:
    """
    Load existing local CSV as a time-indexed DataFrame, or return empty DF.
    """
    if os.path.exists(file_path):
        df = pd.read_csv(file_path, index_col=0, parse_dates=True)
        df.index.name = "Date"
        return df.sort_index()
    else:
        return pd.DataFrame()

def update_local_data(symbol: str,
                      file_path: str,
                      interval: str = "1d",
                      lookback_days: int = 7) -> pd.DataFrame:
    """
    Read local CSV (or none), fetch only missing rows, append,
    and write back to CSV. Returns the updated DataFrame.
    """
    existing = load_local_csv(file_path)
    today = pd.Timestamp.utcnow().floor("D")

    if not existing.empty:
        last_date = existing.index.max()
        # If last date is today's date, assume data is up-to-date
        if last_date >= today:
            print(f"[{symbol}] Local data up-to-date through {last_date.date()}")
            return existing
        start = last_date - pd.Timedelta(days=lookback_days)
    else:
        start = today - pd.Timedelta(days=365 * 1)  # default to 1 year
    print(f"[{symbol}] Downloading new data from {start.date()} to {today.date()}")

    new = download_symbol_data(symbol=symbol, start_date=start, end_date=today, interval=interval)

    if new.empty:
        print(f"[{symbol}] No new data downloaded.")
        return existing

    combined = pd.concat([existing, new])
    combined = combined[~combined.index.duplicated(keep="last")].sort_index()
    combined.to_csv(file_path)
    print(f"[{symbol}] Updated local data: {len(existing)} → {len(combined)} rows saved to {file_path}")

    return combined
