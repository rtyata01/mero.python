# Logistic regression, use score input to predice the pass or failure (1,0) binary outcome
# Split the data, so the model can learn from 80% and be tested on the remaining 20%.
# Formula = 1 / (1 + e^-(mx + b))

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Simulated data
# Lower score results failure, higher score 55 and above results success.
data = pd.DataFrame({
    'Score': [40, 45, 50, 55, 60, 65, 70, 75, 80, 85],
    'Passed': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]  # 0 = Fail, 1 = Pass
})

# Features and target
X = data[['Score']]
y = data['Passed']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict and evaluate
predictions = model.predict(X_test)
print("Predictions:", predictions)
print("Accuracy:", accuracy_score(y_test, predictions))
