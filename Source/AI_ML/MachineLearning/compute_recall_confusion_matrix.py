# Recall measures how well your model finds all the positive cases.
# Recall Formula = TP // (TP + FN)

# Confusion Matrix is a table used to describe the performance of a classification model by showing the actual vs. predicted classes.
"""
|                 | Predicted Positive  | Predicted Negative  |
| --------------- | ------------------- | ------------------- |
| Actual Positive | True Positive (TP)  | False Negative (FN) |
| Actual Negative | False Positive (FP) | True Negative (TN)  |
"""

from sklearn.metrics import confusion_matrix, recall_score

# Actual labels
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]

# Predicted labels
y_pred = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]

# Compute confusion matrix
cm = confusion_matrix(y_true, y_pred)
print("Confusion Matrix:\n", cm)

# Compute recall
recall = recall_score(y_true, y_pred)
print("Recall:", recall)
