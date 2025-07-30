# Medium - Compute the minimum possible difference between the largest and smallest values in a list nums 
# after making at most max_changes replacements (modifications of values).
# Given n numbers, replace any X=3 numbers, and find the min diff between smallest and largest.

import heapq

def heap_min_difference(nums, max_changes):
    if len(nums) <= max_changes + 1:
        return 0

    smallest_vals = heapq.nsmallest(max_changes + 1, nums)
    largest_vals = heapq.nlargest(max_changes + 1, nums)

    return min(
        largest_vals[max_changes - i] - smallest_vals[i]
        for i in range(max_changes + 1)
    )

# Time Complexity: O(n log k)
    # heap = O(n log k)
    # loop = O (k + 1)
# Space Complexity: O(k)

def sorted_min_difference(nums, maxChanges):
    n = len(nums)
    
    if n <= maxChanges + 1:
        return 0  # can make all equal or nearly equal
    
    sorted_nums = sorted(nums) # sort the numbers in ascending order.
    
    window_size = n - maxChanges
    return min(
        sorted_nums[i + window_size - 1] - sorted_nums[i] 
        for i in range(maxChanges + 1)
    )

# Time Complexity: O(n log n)
    # heap = O(n log n)
    # loop = O (k + 1)
# Space Complexity: O(1)

nums = [1, 5, 6, 14]  # [1, 1, 1, 1]
replaceNumbers = 3
# Window size = 4-3 = 1, need at least 2 elements for computing difference, so return 0
print(f"Expected heap min difference: 0, Computed: {heap_min_difference(nums, replaceNumbers)}")
print(f"Expected sorted min difference: 0, Computed: {sorted_min_difference(nums, replaceNumbers)}")

nums = [1, 5, 6, 14, 15]  # [5, 5, 6, 5, 5]
replaceNumbers = 3
# window size = 5-3= 2, [1,5]=4, [5,6]=1, [6,14]=8, [14,15]=1 
# min(4,1,8,1) = 1
print(f"Expected heap min difference: 1, Computed: {heap_min_difference(nums, replaceNumbers)}")
print(f"Expected sorted min difference: 1, Computed: {sorted_min_difference(nums, replaceNumbers)}")

nums = [1, 5, 7, 14, 15, 18]  # [14, 14, 14, 15, 18] = 18 - 14 = 4, [1, 5, 7, 7, 7, 7] = 7 - 1 = 6
replaceNumbers = 3
print(f"Expected heap min difference: 4, Computed: {heap_min_difference(nums, replaceNumbers)}")
print(f"Expected sorted min difference: 4, Computed: {sorted_min_difference(nums, replaceNumbers)}")

"""
min_heap = heapq.nsmallest(4, nums) → [1, 5, 7, 14]
max_heap = heapq.nlargest(4, nums)  → [18, 15, 14, 7]

#sort = [1, 5, 7, 14, 15, 18]

#comparision use:

Range	    Difference
1 to 7	    6
5 to 14	    9
7 to 15	    8
14 to 18	4 

"""