# Count how many contiguous subarrays of nums, whose sum is exactly equal to k.
# Works with negative number as well.

# subarray_sum for nums[i+1...j] = prefix_sum[j] - prefix_sum[i]
# prefix_sum[i] = prefix_sum[j] - target

from collections import defaultdict
from typing import List

def find_contiguous_subarrays_with_sum(nums: List[int], target: int) :
    prefix_sum = 0
    subarrays = []
    sum_to_indices = defaultdict(list)
    sum_to_indices[0].append(-1)  # Starting with sum = 0, at index -1

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

def find_subsets_with_sum(nums: List[int], target: int) -> List[List[int]]:
    """Find all subsets of any size whose sum equals the target."""
    
    result = []

    def backtrack(start: int, path: List[int], current_sum: int):
        # Check if current subset matches the target
        if current_sum == target:
            result.append(path.copy())
            # Continue searching for other subsets
        # Explore remaining elements
        for i in range(start, len(nums)):
            # Include nums[i] in the subset
            path.append(nums[i])
            backtrack(i + 1, path, current_sum + nums[i])
            path.pop()  # backtrack

    backtrack(0, [], 0) # start index, path, sum
    
    # Remove empty subset(s)
    result = [subset for subset in result if subset]
    return result

# Tests
test_cases = [
    ([1, -1, 0, -2 , 2], 0),
    ([1, 2, 0, 3, -1], 3),
    ([1, 1, 1], 2),
    ([3, 2, 1], 15)
]

for arr, target_sum in test_cases:
    result = find_contiguous_subarrays_with_sum(arr, target_sum)
    print(f"Contiguous Subarray - Input: {arr} and sum: {target_sum}, subarray count: {len(result)}, subarrays: {result}")

# sum_to_indices = {0: [-1]}
# i=0, sum_to_indices = {0: [-1], 1: [0]}
# i=1, sum_to_indices = {0: [-1, 1], 1: [0]}, Subarray: nums[0:2] = [1, -1] 
# i=2, sum_to_indices = {0: [-1, 1, 2], 1: [0]}, Subarrays: nums[0:3] = [1, -1, 0], nums[2:3] = [0]
# i=3, sum_to_indices = {0: [-1, 1, 2], 1: [0], -2: [3]}
# i=4, sum_to_indices = {0: [-1, 1, 2, 4], 1: [0], -2: [3]}, subarrays: [1, -1, 0, -2, 2], [0, -2, 2], [-2, 2]

for arr, target_sum in test_cases:
    result = find_subsets_with_sum(arr, target_sum)
    print(f"Subsets - input: {arr} and sum: {target_sum}, subarray count: {len(result)}, subarrays: {result}")
