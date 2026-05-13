import numpy as np

# Sample dataset: exam scores of 10 students
scores = [88, 92, 79, 93, 85, 91, 87, 90, 84, 89]

# Mean (average)
mean_score = np.mean(scores)

# Median (middle value)
median_score = np.median(scores)

# Variance (measure of spread)
variance_score = np.var(scores, ddof=1)  # ddof=1 for sample variance

# Standard Deviation (spread in same units as data)
std_dev_score = np.std(scores, ddof=1)

print(f"Scores: {scores}")
print(f"Mean: {mean_score}")
print(f"Median: {median_score}")
print(f"Variance: {variance_score}")
print(f"Standard Deviation: {std_dev_score}")