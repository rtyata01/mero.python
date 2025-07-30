# Count how many contiguous subarrays of nums, whose sum is exactly equal to k.
# Works with negative number as well.

from collections import defaultdict
from typing import List

def find_subarrays_with_sum(nums: List[int], target: int) :
    prefix_sum = 0
    subarrays = []
    sum_to_indices = defaultdict(list)
    sum_to_indices[0].append(-1)  # Handles subarrays starting at index 0

    for index, value in enumerate(nums):
        prefix_sum += value
        required_sum = prefix_sum - target

        for start_index in sum_to_indices.get(required_sum, []):  # if required_sum in sum_to_indices: is not preferred.
            subarrays.append(nums[start_index + 1 : index + 1])

        sum_to_indices[prefix_sum].append(index)

    return subarrays

    # Time Complexity: 
        # Best case : O(n)
        # Worst case : O(n²), if there are many repeated prefix sums.
    # Space Complexity: 
        # worst	= O(n²)

def find_subarrays_with_sum_brute_force(nums, target):
    result = []
    n = len(nums)

    for start in range(n):
        current_sum = 0
        subarray = []

        for end in range(start, n):
            current_sum += nums[end]
            subarray.append(nums[end])

            if current_sum == target:
                result.append(subarray[:])  # Copy current subarray (O(k), but done only for matches)

    return result

    # Time Complexity: O(n²)
        # Loop: O(n²)
        # Copying subarrays:  O(k) per matching subarray.
    # Space Complexity: 
        # worst	= O(n³)

# Tests
test_cases = [
    ([1, -1, 0, -2 , 2], 0),
    ([1, 2, 3], 3),
    ([1, 1, 1], 2),
    ([3, 2, 1], 15)
]

for arr, target_sum in test_cases:
    result = find_subarrays_with_sum(arr, target_sum)
    print(f"Input: {arr} and sum: {target_sum}, subarray count: {len(result)}, subarrays: {result}")

# sum_to_indices = {0: [-1]}
# i=0, sum_to_indices = {0: [-1], 1: [0]}
# i=1, sum_to_indices = {0: [-1, 1], 1: [0]}, Subarray: nums[0:2] = [1, -1] 
# i=2, sum_to_indices = {0: [-1, 1, 2], 1: [0]}, Subarrays: nums[0:3] = [1, -1, 0], nums[2:3] = [0]
# i=3, sum_to_indices = {0: [-1, 1, 2], 1: [0], -2: [3]}
# i=4, sum_to_indices = {0: [-1, 1, 2, 4], 1: [0], -2: [3]}, subarrays: [1, -1, 0, -2, 2], [0, -2, 2], [-2, 2]

for arr, target_sum in test_cases:
    result = find_subarrays_with_sum_brute_force(arr, target_sum)
    print(f"Brute force approach input: {arr} and sum: {target_sum}, subarray count: {len(result)}, subarrays: {result}")
