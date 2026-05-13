import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Hours studied (reshape for sklearn)
y = np.array([50, 55, 65, 70, 75])           # Exam scores

# Create model, y = mx+c
model = LinearRegression()

# Train model
model.fit(X, y)

# Get coefficients
slope = model.coef_[0]
intercept = model.intercept_
print(f"Regression equation: y = {slope:.2f}x + {intercept:.2f}")

# Predict exam scores
y_pred = model.predict(X)

# Predict for a new value, e.g., 6 hours
new_hours = np.array([[6]])
predicted_score = model.predict(new_hours)
print(f"Predicted exam score for 6 hours: {predicted_score[0]:.2f}")

plt.scatter(X, y, color='blue', label='Actual Scores')
plt.plot(X, y_pred, color='red', label='Regression Line')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('Linear Regression: Hours vs Exam Score')
plt.legend()
plt.show()