# Linear regression, use size input to predice the price.
# Split the data, so the model can learn from 80% and be tested on the remaining 20%.
# Formula = y = mx + b

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Simulated data
# Size grows, Price also grows linearly on straight line.
data = pd.DataFrame({
    'Size (sq ft)': [500, 1000, 1500, 2000, 2500],
    'Price ($)': [150000, 200000, 250000, 300000, 350000]
})

# Features and target
X = data[['Size (sq ft)']]
y = data['Price ($)']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)
print("Predicted prices:", predictions)
print("MSE:", mean_squared_error(y_test, predictions))

# Plot
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.title("Linear Regression: Size vs. Price")
plt.xlabel("Size (sq ft)")
plt.ylabel("Price ($)")
plt.show()
