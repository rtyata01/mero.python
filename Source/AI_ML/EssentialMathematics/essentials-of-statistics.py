import statistics

scores = [88, 92, 79, 93, 85, 91, 87, 90, 84, 89]

mean_score = statistics.mean(scores)
median_score = statistics.median(scores)
variance_score = statistics.variance(scores)
std_dev_score = statistics.stdev(scores)

print(f"Mean: {mean_score}")
print(f"Median: {median_score}")
print(f"Variance: {variance_score}")
print(f"Standard Deviation: {std_dev_score}")