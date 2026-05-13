import numpy as np
from scipy import stats

# Sample scores from the class
sample_scores = [88, 92, 79, 93, 85, 91, 87, 90, 84, 89, 85]

# Population mean claimed by the teacher
population_mean = 85

# Perform one-sample t-test
t_stat, p_value = stats.ttest_1samp(sample_scores, population_mean)

print(f"T-statistic = {t_stat:.2f}")
print(f"P-value = {p_value:.4f}")

alpha = 0.05  # significance level

if p_value < alpha:
    print("Reject the null hypothesis: The sample mean is significantly different from 85.")
else:
    print("Fail to reject the null hypothesis: No significant difference from 85.")