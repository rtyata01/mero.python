# Decision Tree, use age and salary input, to decide buy decision (0 = No, 1 = yes)
# Split the data, so the model can learn from 75% and be tested on the remaining 25%.
# Formula = y = mx + b


import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 1. Sample dataset 
# lower age and lower salary, buy = No
# higher age and higher salary, buy = yes
data = pd.DataFrame({
    'Age': [22, 25, 47, 52, 46, 56, 55, 60],
    'Salary': [15000, 29000, 48000, 60000, 52000, 61000, 58000, 62000],
    'Buy': [0, 0, 1, 1, 1, 1, 1, 1]  # 0 = No, 1 = Yes
})

# 2. Features and target
X = data[['Age', 'Salary']]  # Input features
y = data['Buy']              # Target label

# 3. Split into training/testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# 4. Train Decision Tree
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 5. Make predictions
predictions = model.predict(X_test)

# 6. Evaluate model
print("Accuracy:", accuracy_score(y_test, predictions))

# 7. Visualize the tree
plt.figure(figsize=(10,6))
plot_tree(model, feature_names=['Age', 'Salary'], class_names=['No', 'Yes'], filled=True)
plt.title("Decision Tree")
plt.show()
