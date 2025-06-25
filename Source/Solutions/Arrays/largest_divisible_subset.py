def largest_divisible_subset(nums):
    if not nums:
        return []

    nums.sort()
    n = len(nums)
    dp = [1] * n           # dp[i] = size of largest subset ending with nums[i]
    prev = [-1] * n        # to reconstruct path

    max_size = 1
    max_index = 0

    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[i] > max_size:
            max_size = dp[i]
            max_index = i

    # Reconstruct subset
    answer = []
    current = max_index
    while current != -1:
        answer.append(nums[current])
        current = prev[current]

    return answer[::-1]  # reverse to get correct order

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
