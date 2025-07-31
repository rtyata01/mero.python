# Kth Nearest Neighbour, with input Age and Salary to Decide on Buy or No-Buy (1 =yes, 0 = No).
# Split the data, so the model can learn from 75% and be tested on the remaining 25%.
# For example, if k=3 and the 3 nearest neighbors are [1, 1, 0], it classifies as 1 (since majority is 1).
# Formula Distance = sqroot (x1-x2)^2 + (y1-y2)^2

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. Create dataset
data = pd.DataFrame({
    'Age': [22, 25, 47, 52, 46, 56, 55, 60],
    'Salary': [15000, 29000, 48000, 60000, 52000, 61000, 58000, 62000],
    'Buy': [0, 0, 1, 1, 1, 1, 1, 1]  # 0 = No, 1 = Yes
})

# 2. Define features and target
X = data[['Age', 'Salary']]  # inputs
y = data['Buy']              # output

# 3. Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# 4. Create and train KNN model
model = KNeighborsClassifier(n_neighbors=3)  # Try 3 nearest neighbors
model.fit(X_train, y_train)

# 5. Make predictions
predictions = model.predict(X_test)

# 6. Evaluate
print("Predictions:", predictions)
print("Actual:", list(y_test))
print("Accuracy:", accuracy_score(y_test, predictions))
