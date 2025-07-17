# Find the Largest Divisible Subset using DFS with memoization.

class Solution:
    def largest_divisible_subset(self, nums):
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        cache = {}

        def dfs_recurse(i):
            if i in cache:
                return cache[i]

            max_subset = [nums[i]]  # start with nums[i] itself

            for j in range(i + 1, n):
                if nums[j] % nums[i] == 0:
                    candidate = dfs_recurse(j)
                    if len(candidate) + 1 > len(max_subset):
                        max_subset = [nums[i]] + candidate

            cache[i] = max_subset
            return max_subset

        largest_subset = []
        for i in range(n):
            subset = dfs_recurse(i)
            if len(subset) > len(largest_subset):
                largest_subset = subset

        return largest_subset

sol = Solution()
nums = [1, 2, 4, 8]
print(sol.largest_divisible_subset(nums))  # Output: [1, 2, 4, 8]

# Use the Recursive + Memoization version when:
# You prefer a more elegant, functional-style solution.
# You want something easy to read and reason about.
# Your inputs are moderate (e.g. n <= 1000) and stack depth isn't an issue.

nums = [1, 3, 6, 9, 18]
print(sol.largest_divisible_subset(nums))  # output [1, 3, 6, 18]

nums = [2, 2, 2, 2, 2]
print(sol.largest_divisible_subset(nums))  # output [2, 2, 2, 2, 2]