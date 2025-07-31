# Accuracy = Overall correctness of the model
# Accuracy Formual = (TP + TN) // (TP + TN + FP + FN), T is true, F is flase, P is positive, N is negative.

# Precision = Of all predicted positives, how many were correct.
# Precision Formula = TP // (TP + FP)

from sklearn.metrics import accuracy_score, precision_score

# Actual values
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]

# Model predictions
y_pred = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]

# Calculate accuracy and precision
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
