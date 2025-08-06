# run_agent.py
import os
import logging
from screener_utils import init_cache_db
from screen_by_volume import find_high_volume_stocks, save_volume_tickers_to_db
from screen_by_price import find_stocks_with_rising_prices, save_increasing_price_tickers
from stock_data_utils import update_local_data

# -------------------- Configuration --------------------
DATA_DIR = "data"
TOP20_SCREEN_STOCKS = "top20_screened_stocks.csv"

# -------------------- Logging --------------------
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# -------------------- Main --------------------
def main():
    
    # Step A: Screen by increasing volume.
    init_cache_db()
    screen_by_volume = find_high_volume_stocks()
    save_volume_tickers_to_db(screen_by_volume)
    logger.info(f"Completed screen by volume and updated database with {len(screen_by_volume)} stocks")
    
    # Step B: Screen by increasing price.
    screen_by_price = find_stocks_with_rising_prices()
    save_increasing_price_tickers(screen_by_price)
    logger.info(f"Completed screen by price and updated stock_price_cache with {len(screen_by_price)} stocks")
    
    # Step C: Select top 20 stocks
    # (symbol, stock_name, price, volume, has_increasing_price)
    filtered = [row for row in screen_by_price if row[4] == True]

    # Sort by volume (index 3), then price (index 2, Optional[float])
    sorted_data = sorted(
        filtered,
        key=lambda x: (x[3], x[2] if x[2] is not None else float('inf'))
    )

    screened = sorted_data[:20]
    print(f"Screened {len(screened)} tickers: {screened}")

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
