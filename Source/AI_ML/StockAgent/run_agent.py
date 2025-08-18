# Screen stocks for short term gains, with better fundamentals, price, volume and quality.

import os
import time
import logging
import pandas as pd
from datetime import datetime
from pathlib import Path
from screener_utils import init_cache_db
from screen_by_fundamental import find_trending_stocks, save_trending_tickers_to_db
from screen_by_volume import find_high_volume_stocks, save_volume_tickers_to_db
from screen_by_price import find_increasing_price_stocks, save_price_tickers_to_db
from screen_by_quality import find_quality_stocks, save_quality_tickers_to_db
from model_train_predict_quality import train_predict_quality_stocks, save_predicted_tickers_to_db

# -------------------- Configuration --------------------
DATE_FORMAT = "%Y%m%d"
DATA_DIR = "data"

# -------------------- Logging --------------------
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# -------------------- CSV Save Utility --------------------
def save_lists_to_csv(column_names, *lists):
    """Save multiple lists into a CSV file with custom column names."""
    if len(column_names) != len(lists):
        raise ValueError("Number of column names must match number of lists.")

    max_len = max(len(lst) for lst in lists)
    padded_lists = [sorted(list(lst)) + [None] * (max_len - len(lst)) for lst in lists]
    df = pd.DataFrame({name: data for name, data in zip(column_names, padded_lists)})
    
    date_str = datetime.today().strftime(DATE_FORMAT)
    filename_with_date = f"screened_stocks_{date_str}.csv"
    file_name = os.path.join(Path(__file__).resolve().parent, DATA_DIR, filename_with_date)
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    
    df.to_csv(file_name, index=False)
    logger.info(f"CSV saved as {filename_with_date}")

# -------------------- Main --------------------
def main():
    start_time = time.time()

    logger.info("Starting stock screening process...")
    init_cache_db()

    # Step A: Trending stocks
    logger.info("Screening trending stocks...")
    trending_stocks = find_trending_stocks(monthly_screen=False)
    save_trending_tickers_to_db(trending_stocks)
    logger.info(f"Trending stocks found: {len(trending_stocks)}")

    # Step B1: High volume
    logger.info("Screening high volume stocks...")
    high_volume = find_high_volume_stocks()
    save_volume_tickers_to_db(high_volume)
    logger.info(f"High volume stocks: {len(high_volume)}")

    # Step B2: Rising price
    logger.info("Screening rising price stocks...")
    rising_price = find_increasing_price_stocks()
    save_price_tickers_to_db(rising_price)
    logger.info(f"Rising price stocks: {len(rising_price)}")

    # Step B3: High quality
    logger.info("Screening high quality stocks...")
    high_quality = find_quality_stocks()
    save_quality_tickers_to_db(high_quality)
    logger.info(f"High quality stocks: {len(high_quality)}")

    # Step C: Predict quality
    logger.info("Predicting high quality stocks...")
    predicted_quality = train_predict_quality_stocks()
    save_predicted_tickers_to_db(predicted_quality)
    logger.info(f"Predicted quality stocks: {len(predicted_quality)}")

    # Step D: Save results to CSV
    save_lists_to_csv(
        ["Rising Volume", " Rising Price", " Short-Term Profit", " Predicted Short-Term Profit"],
        {row[0] for row in high_volume},
        {row[0] for row in rising_price},
        {row[0] for row in high_quality},
        {row[0] for row in predicted_quality}
    )

    elapsed_str = time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))
    logger.info(f"Completed stock screening in {elapsed_str}")

if __name__ == "__main__":
    main()
