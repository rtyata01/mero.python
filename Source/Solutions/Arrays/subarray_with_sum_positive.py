# Count how many contiguous subarrays of nums, whose sum is exactly equal to k.

# Works only for positive numbers.
def subarray_sum_positive(nums, k):
    count = 0
    left = 0
    current_sum = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        # Shrink the window until current_sum <= k
        while current_sum > k:
            current_sum -= nums[left]
            left += 1

        if current_sum == k:
            count += 1

    return count

from collections import defaultdict

def subarray_sum(nums, k):
    count = 0
    current_sum = 0
    prefix_sums = defaultdict(int)
    prefix_sums[0] = 1  # Base case: subarray starts from index 0

    for num in nums:
        current_sum += num
        count += prefix_sums[current_sum - k]
        prefix_sums[current_sum] += 1

    return count


arr = [1, 2, 3]
# 1, 3 count=1, 6, 6-1, 5-2, 3 count = 2     
print(f"expected: 2, result: ", subarray_sum_positive(arr, 3))

arr = [1, 1, 1]    
print(f"expected: 2, result: ", subarray_sum_positive(arr, 2))

nums = [1, -1, 2, 3]
print(f"expected: 1, result: ", subarray_sum_positive(arr, 3))