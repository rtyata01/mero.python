import heapq
# Given n numbers, replace any 3 numbers and find the min diff between smallest and largest.


def heap_min_difference(nums, maxChanges):
    n = len(nums)
    
    if n <= maxChanges + 1:
        return 0  # Can change all to same number
    
    # Get 4 smallest using heap
    min_heap = heapq.nsmallest(maxChanges + 1, nums)
    max_heap = heapq.nlargest(maxChanges + 1, nums)
    
    # Try all 4 change combinations
    min_diff = float('inf')
    for i in range(maxChanges + 1):
        smallest = min_heap[i]  # i smallest values replaced
        largest = max_heap[maxChanges - i]  # (k - i) largest values replaced
        min_diff = min(min_diff, largest - smallest)
    
    return min_diff

def sorted_min_difference(nums, maxChanges):
    n = len(nums)
    
    if n <= maxChanges + 1:
        return 0  # can make all equal or nearly equal
    
    nums.sort()
    
    min_diff = float('inf')
    for i in range(maxChanges + 1):
        diff = nums[(n - 1) - (maxChanges - i)] - nums[i]
        if diff < min_diff:
            min_diff = diff

    return min_diff

nums = [1, 5, 6, 14]  # [1, 1, 1, 1]
replaceNumbers = 3
print(f"Expected heap min difference: 0, Computed: {heap_min_difference(nums, replaceNumbers)}")
print(f"Expected sorted min difference: 0, Computed: {sorted_min_difference(nums, replaceNumbers)}")

nums = [1, 5, 6, 14, 15]  # [5, 5, 6, 5, 5]
replaceNumbers = 3
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