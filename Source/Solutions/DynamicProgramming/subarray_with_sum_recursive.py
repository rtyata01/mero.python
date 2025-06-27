# Count how many contiguous subarrays of nums, whose sum is exactly equal to k.
# Works with negative number as well.
from collections import defaultdict

class Solution:
    def find_subarrays_with_sum(self, nums, target, cache=None):
        if cache is None:
            cache = {}

        def dfs(start):
            if start >= len(nums):
                return []  # no subarrays

            if start in cache:
                return cache[start]

            result = []
            current_sum = 0

            # Extend subarray from start to end
            for end in range(start, len(nums)):
                current_sum += nums[end]
                if current_sum == target:
                    result.append(nums[start:end + 1])

            # Recurse for next start index
            next_result = dfs(start + 1)
            result.extend(next_result)

            cache[start] = result
            return cache[start]

        return dfs(0)  #start with 0 i.e. frist num.

# Example usage
sol = Solution()
arr = [1, -1, 0, -2, 2]
target_sum = 0
subarrays = sol.find_subarrays_with_sum(arr, target_sum)
print(f"Count: {len(subarrays)}")
print("Subarrays with sum =", target_sum)
for sub in subarrays:
    print(sub)

# [1, -1, 0, -2, 2], [0, -2, 2], [-2, 2]
