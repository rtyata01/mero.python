# Find the Largest Divisible Subset.

# Can be solved using:
    # recursive approach = top-down approach.
    # dynamice programming approach = bottom-up approach.

# dp[i] stores the size of largest subset
# prev[i] stores the index of previous element in the subset.

def largest_divisible_subset(nums):
    if not nums:
        return []

    nums.sort()
    n = len(nums)
    dp = [1] * n         # dp[i] = size of largest subset ending at nums[i]
    prev = [-1] * n      # prev[i] = index of previous element in the subset

    max_index = 0        # Index of the largest element in the best subset

    for i in range(n):
        for j in range(i):  # Only consider elements before i
            if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[i] > dp[max_index]:
            max_index = i

    # Reconstruct the largest divisible subset
    subset = []
    while max_index != -1:
        subset.append(nums[max_index])
        max_index = prev[max_index]

    return subset[::-1]  # Reverse to return in ascending order

# Time Complexity: O(nlogn) + O(n^2) + O(n) = O(n^2)
# Space Complexity: O(n)

# Example usage:
nums = [1, 2, 4, 8]
print(largest_divisible_subset(nums))  # Output: [1, 2, 4, 8]

# dp = [1,1,1,1], prev = [-1,-1,-1,-1]
# i = 1, nums[1] = 2
# j = 0, nums[0] = 1, 2 % 1 = 0, dp[1] = dp[0] + 1 = 2, prev[2] = 0
# dp = [1, 2, 1, 1], prev = [-1, 0, -1, -1]
# max_size = 2, max_index = 1

# i = 2, nums[2] = 4
# j = 0, nums[0] = 1, 4 % 1 = 0, dp[2] = dp[0] + 1 = 2, prev[2] = 0
# dp = [1, 2, 2, 1], prev = [-1, 0, 0, -1]
# j = 1, nums[0] = 2, 4 % 2 = 0, dp[2] = dp[1] + 1 = 3, prev[2] = 1
# dp = [1, 2, 3, 1], prev = [-1, 0, 1, -1]
# max_size = 3, max_index = 2

# i = 3, nums[3] = 8
# j = 0, nums[0] = 1, 8 % 1 = 0, dp[3] = dp[0] + 1 = 2, prev[3] = 0
# dp = [1, 2, 3, 2], prev = [-1, 0, 1, 0]
# j = 1, nums[0] = 2, 8 % 2 = 0, dp[3] = dp[1] + 1 = 3, prev[3] = 1
# dp = [1, 2, 3, 3], prev = [-1, 0, 1, 1]
# j = 2, nums[0] = 2, 8 % 4 = 0, dp[3] = dp[2] + 1 = 4, prev[3] = 2
# dp = [1, 2, 3, 4], prev = [-1, 0, 1, 2]
# max_size = 4, max_index = 

# print nums[3] = 8, nums[prev[3]] = nums[2] = 4, nums[prev[2]] = nums[1] = 2, nums[prev[1]] = 1

# Example usage:
nums = [1, 2, 3, 9]
print(largest_divisible_subset(nums))  # Output: [1, 3, 9]

nums = [1, 2, 3, 4, 8, 9]
print(largest_divisible_subset(nums))  # Output: [1, 2, 4, 8]

# Use the Bottom-Up Iterative DP version when:
# You want maximum performance.
# You want fine control over path reconstruction.
# You're solving a version with huge input sizes.
# You're extending it to track additional things (e.g., subset count, subset sum).