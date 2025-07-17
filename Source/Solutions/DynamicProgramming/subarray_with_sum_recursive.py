# Count how many contiguous subarrays of nums, whose sum is exactly equal to k.
# Works with negative number as well.
from collections import defaultdict

class Solution:
    def print_subarrays_with_sum(self, nums, target):
        subarrays = self.find_subarrays_with_sum(nums, target)
        print(f"Count: {len(subarrays)}")
        print("Subarrays with sum = ", target)
        for sub in subarrays:
            print(sub)
            
    def find_subarrays_with_sum(self, nums, target):
        subarrays = []
        n = len(nums)

        for start in range(n):
            current_sum = 0
            for end in range(start, n):
                current_sum += nums[end]
                if current_sum == target:
                    subarrays.append(nums[start:end + 1])
        
        return subarrays
    
    def find_subarrays_with_sum_recursive(self, nums, target, cache=None):
        if cache is None:
            cache = {}

        def find_matching_sum(start):
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
            next_result = find_matching_sum(start + 1)
            result.extend(next_result)

            cache[start] = result
            return cache[start]

        return find_matching_sum(start=0)  #start with 0 i.e. frist num.

# Example usage
sol = Solution()
sol.print_subarrays_with_sum([1, -1, 0, -2, 2], 0) # [1, -1, 0, -2, 2], [0, -2, 2], [-2, 2]
sol.print_subarrays_with_sum([1, 2, 3], 3) # [1,2], [3]
sol.print_subarrays_with_sum([1, 1, 1], 2) # [1,1], [1,1]
