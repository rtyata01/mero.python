# Dependecies
pip install --upgrade pip
pip install yfinance pandas numpy
pip install scikit-learn matplotlib
pip install yahooquery

.1. 📥 Data Collection
Data Type	Source	Example
Stock Price & Volume (intraday or daily)	yfinance, pandas_datareader, Alpaca	yf.download("AAPL", start="2015-01-01", interval="1m")
Call vs Put Trading Volume	CBOE daily/equity put–call ratio or API	aggregate calls and puts to compute PCR 

Order Flow (Buy vs Sell Volume)	Level‑2 feed or historical trades with side (the US “trades” dataset) or REST API	compute buy- and sell- volume per second
VWAP	Calculate per minute/day as (price × vol).cumsum() / volume.cumsum() 
SaxaFund
Wikipedia


2. 🔧 Feature Engineering (by Time Window, e.g. 1-minute / 5-minute periods)
text
Copy
Edit
| timestamp | price | volume | VWAP | price_to_vol = price / volume |
|-----------|-------|--------|------|-------------------------------|
| …         | …     | …      | …    | …                             |
| call_vol  | put_vol | pcr = put_vol / call_vol | order_imbalance | price_change_t+1 |
Price-to-Volume Ratio: captures magnitude of price change relative to liquidity (more predictive than raw volume)

PCR (Put–Call Ratio): gauge of bearish or bullish options sentiment; has demonstrated next-day predictive power especially at extremes 

VWAP: helps normalize price relative to where most volume traded—prices below VWAP may indicate undervaluation, vice versa 

Order Flow Imbalance: buy/sell skew impacts microstructure price discovery strongly over short horizons 
arxiv.org

Combine these with lagged features (e.g. Δprice_to_vol_t−1, ΔPCR_t−1, moving averages of imbalance) to capture momentum.

3. 🧠 Modeling
Regression target: next-period log-return or price

Classification target (optional): direction of price change > threshold (e.g. >0.1%)

Use RandomForestRegressor, XGBoost, or lightweight neural networks on feature windows

For intraday predictions, you can augment with temporal architecture like LSTM or time-series cross-section models

Example: Python & scikit-learn:

python
Copy
Edit
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import TimeSeriesSplit
features = ['price_to_vol','VWAP','pcr','order_imbalance','lag1_poV','lag1_pcr']
X = df[features]
y = df['price_t+1']
tscv = TimeSeriesSplit(n_splits=5)
for train_idx, val_idx in tscv.split(X):
  X_tr, X_val = X.iloc[train_idx], X.iloc[val_idx]
  y_tr, y_val = y.iloc[train_idx], y.iloc[val_idx]
  model = RandomForestRegressor(n_estimators=100, random_state=42)
  model.fit(X_tr, y_tr)
  val_pred = model.predict(X_val)
  # evaluate
Use walk‑forward validation due to non‑stationarity: sliding window training and testing to mimic live deployment.

4. ✅ Evaluation
Regression metrics: RMSE, MAE, directional accuracy

Benchmark: persistence model (predict next price = current price) + 1-day forward naïve

Backtest-style test: simulate profit by “betting long when PCR < 0.7 and price below VWAP that reverses next tick” or “short when order imbalance > +0.2”

Visualize results: Price vs Predicted, feature importances (PCR or imbalance may score high).

5. 🎯 Sample End-to-End Code Sketch
python
Copy
Edit
import yfinance as yf
import pandas as pd

df = yf.download('AAPL', start='2022-01-01', end='2022-03-01', interval='5m')
# assume we loaded call/put volume to df['call_vol'], df['put_vol']
df['pcr'] = df['put_vol'] / (df['call_vol'] + 1e-6)
df['typ_price'] = (df['High'] + df['Low'] + df['Close'])/3
df['pv'] = df['typ_price'] * df['Volume']
df['cum_pv'] = df['pv'].cumsum()
df['cum_vol'] = df['Volume'].cumsum()
df['VWAP'] = df['cum_pv'] / df['cum_vol']
df['price_to_vol'] = df['Close'] / (df['Volume'] + 1e-6)
df['order_imbalance'] = (df['buy_vol'] - df['sell_vol']) / (df['buy_vol'] + df['sell_vol'] + 1e-6)
df['target'] = df['Close'].shift(-1) / df['Close'] - 1
df.dropna(inplace=True)
Train/test split and modeling follow as above.

6. 🧾 Why This Approach Works
PCR is a well-known sentiment proxy — low PCR precedes short-term outperformance and vice versa. Has contrarian predictive edge 

Price-to-volume features normalize price movement relative to liquidity and volatility.

Order imbalance creates directional pressure that often drives micro-level price moves faster than volume alone 

VWAP aligns price to where heavier volume trades helping normalize value expectations intraday

2. 🔧 Feature Engineering (by Time Window, e.g. 1-minute / 5-minute periods)
text
Copy
Edit
| timestamp | price | volume | VWAP | price_to_vol = price / volume |
|-----------|-------|--------|------|-------------------------------|
| …         | …     | …      | …    | …                             |
| call_vol  | put_vol | pcr = put_vol / call_vol | order_imbalance | price_change_t+1 |
Price-to-Volume Ratio: captures magnitude of price change relative to liquidity (more predictive than raw volume)

PCR (Put–Call Ratio): gauge of bearish or bullish options sentiment; has demonstrated next-day predictive power especially at extremes 

VWAP: helps normalize price relative to where most volume traded—prices below VWAP may indicate undervaluation, vice versa 

Order Flow Imbalance: buy/sell skew impacts microstructure price discovery strongly over short horizons 
arxiv.org

Combine these with lagged features (e.g. Δprice_to_vol_t−1, ΔPCR_t−1, moving averages of imbalance) to capture momentum.

3. 🧠 Modeling
Regression target: next-period log-return or price

Classification target (optional): direction of price change > threshold (e.g. >0.1%)

Use RandomForestRegressor, XGBoost, or lightweight neural networks on feature windows

For intraday predictions, you can augment with temporal architecture like LSTM or time-series cross-section models

Example: Python & scikit-learn:

python
Copy
Edit
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import TimeSeriesSplit
features = ['price_to_vol','VWAP','pcr','order_imbalance','lag1_poV','lag1_pcr']
X = df[features]
y = df['price_t+1']
tscv = TimeSeriesSplit(n_splits=5)
for train_idx, val_idx in tscv.split(X):
  X_tr, X_val = X.iloc[train_idx], X.iloc[val_idx]
  y_tr, y_val = y.iloc[train_idx], y.iloc[val_idx]
  model = RandomForestRegressor(n_estimators=100, random_state=42)
  model.fit(X_tr, y_tr)
  val_pred = model.predict(X_val)
  # evaluate
Use walk‑forward validation due to non‑stationarity: sliding window training and testing to mimic live deployment.

4. ✅ Evaluation
Regression metrics: RMSE, MAE, directional accuracy

Benchmark: persistence model (predict next price = current price) + 1-day forward naïve

Backtest-style test: simulate profit by “betting long when PCR < 0.7 and price below VWAP that reverses next tick” or “short when order imbalance > +0.2”

Visualize results: Price vs Predicted, feature importances (PCR or imbalance may score high).

5. 🎯 Sample End-to-End Code Sketch
python
Copy
Edit
import yfinance as yf
import pandas as pd

df = yf.download('AAPL', start='2022-01-01', end='2022-03-01', interval='5m')
# assume we loaded call/put volume to df['call_vol'], df['put_vol']
df['pcr'] = df['put_vol'] / (df['call_vol'] + 1e-6)
df['typ_price'] = (df['High'] + df['Low'] + df['Close'])/3
df['pv'] = df['typ_price'] * df['Volume']
df['cum_pv'] = df['pv'].cumsum()
df['cum_vol'] = df['Volume'].cumsum()
df['VWAP'] = df['cum_pv'] / df['cum_vol']
df['price_to_vol'] = df['Close'] / (df['Volume'] + 1e-6)
df['order_imbalance'] = (df['buy_vol'] - df['sell_vol']) / (df['buy_vol'] + df['sell_vol'] + 1e-6)
df['target'] = df['Close'].shift(-1) / df['Close'] - 1
df.dropna(inplace=True)
Train/test split and modeling follow as above.

6. 🧾 Why This Approach Works
PCR is a well-known sentiment proxy — low PCR precedes short-term outperformance and vice versa. Has contrarian predictive edge 

Price-to-volume features normalize price movement relative to liquidity and volatility.

Order imbalance creates directional pressure that often drives micro-level price moves faster than volume alone 

VWAP aligns price to where heavier volume trades helping normalize value expectations intraday