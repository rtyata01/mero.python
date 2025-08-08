# Find stocks with greater fundamentals with rising price and volume.

import os
import time
from datetime import datetime, timedelta
import logging
from screener_utils import init_cache_db
from screen_by_fundamental import find_trending_stocks, save_trending_tickers_to_db
from screen_by_volume import find_high_volume_stocks, save_volume_tickers_to_db
from screen_by_price import find_increasing_price_stocks, save_price_tickers_to_db
from stock_data_utils import update_local_data

# -------------------- Configuration --------------------
DATA_DIR = "data"
TOP20_SCREEN_STOCKS = "top20_screened_stocks.csv"

# -------------------- Logging --------------------
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# -------------------- Main --------------------
def main():
    
    start_time = time.time()
    logger.info(f"Screening trending stocks ...")
    
    # Step A: Screen by increasing volume.
    init_cache_db()
    tickers = find_trending_stocks()
    save_trending_tickers_to_db(tickers)
    logger.info(f"Completed screening {len(tickers)} trending stocks.")
    
    # Step B Screen by increasing volume.
    filtered_by_volume = find_high_volume_stocks()
    save_volume_tickers_to_db(filtered_by_volume)
    logger.info(f"Completed screening {len(filtered_by_volume)} high-volume stocks")
    
    # Step B: Screen by increasing price.
    filtered_by_price = find_increasing_price_stocks()
    save_price_tickers_to_db(filtered_by_price)
    logger.info(f"Completed screening {len(filtered_by_price)} high-price stocks")
    
    # Step C: Select top 20 stocks
    # (symbol, stock_name, price, volume, has_increasing_price)
    price_symbols = {row[0] for row in filtered_by_price if row[4] == True}
    volume_symbols = {row[0] for row in filtered_by_volume if row[4] == True}
    common_symbols = price_symbols & volume_symbols
    filtered_stocks = [row for row in tickers if row[0] in common_symbols]

    # Sort by volume (index 3), then price (index 2, Optional[float])
    sorted_data = sorted(
        filtered_stocks,
        key=lambda x: (x[3], x[2] if x[2] is not None else float('inf'))
    )

    screened = sorted_data[:20]
    print(f"Screened {len(screened)} tickers: {screened}")
    endtime = time.time()
    elapsed_str = time.strftime("%H:%M:%S", time.gmtime(endtime - start_time))
    logger.info(f"Completed stock screener:  {endtime}. Elapsed time: {elapsed_str}")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    top20_screened_file = os.path.join(script_dir, DATA_DIR, TOP20_SCREEN_STOCKS)
    import pandas as pd
    pd.DataFrame({"symbol": screened}).to_csv(top20_screened_file)
    
    # Step D: For each screened ticker, update local data
    #for sym in screened:
     #   csvf = os.path.join(script_dir, DATA_DIR, f"{sym}_1d.csv")
     #   df = update_local_data(symbol=sym, file_path=csvf, interval="1d")
        # Future: call feature engineering / train here

if __name__ == "__main__":
    main()
