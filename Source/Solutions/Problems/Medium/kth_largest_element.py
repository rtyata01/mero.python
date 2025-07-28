# Problem: Find the kth largest element in an unsorted array.

# 1. Using Sorting (simplest alternative)
# 2. Using a Min-Heap Manually (without heapq.nsmallest)
# 3. Using Quickselect (efficient for large lists)

import heapq

def find_kth_largest_builtin(nums, k):
    return heapq.nlargest(k, nums)[-1]

    # heapq.nlargest(3, nums)  # → [9, 8, 7]
    # heapq.nlargest(3, nums)[-1]  # → 7 (3rd largest)
    
# Time Complexity: O(n log k) 
# Space Complexity: O(k)

def find_kth_largest(nums, k):
    min_heap = nums[:k]
    heapq.heapify(min_heap) # list is rearranged into a valid min-heap tree, where parent nodes is smaller than 2 child nodes.
    
    for num in nums[k:]:
        if num > min_heap[0]:  # If current element is larger than the smallest in heap
            heapq.heappop(min_heap) # remove smallest element from min heap, located at position 0.
            heapq.heappush(min_heap, num)
    
    return min_heap[0]

# Time Complexity: O(k + (n - k) * log k) = O(n log k) 
# Space Complexity: O(k)

import random

def find_kth_largest_quickselect(nums, k):
    def quickselect(left, right, index):
        pivot = nums[right]
        p = left
        for i in range(left, right):
            if nums[i] >= pivot:   # note: >= for k-th largest
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
        nums[p], nums[right] = nums[right], nums[p]
        
        if p == index:
            return nums[p]
        elif p < index:
            return quickselect(p + 1, right, index)
        else:
            return quickselect(left, p - 1, index)

    return quickselect(0, len(nums) - 1, k - 1) # k-1 because index is 0-based

# Time Complexity	
    #   best = O(n)
    #   worst = O(n²)
# Space Complexity	
    #   best = O(log n)
    #   worst = O(n)

# Test
arr = [3, 2, 1, 5, 7, 8, 9, 6, 4]
print(f"\n 4th largest elment in: {arr}: ")
print(f"expected: 6, computed:", find_kth_largest(arr, 4))
print(f"expected: 6, computed:", find_kth_largest_builtin(arr, 4)) 

print(f"\n 3rd largest elment in: {arr}: ")
print(f"expected: 7, computed:", find_kth_largest(arr, 3))
print(f"expected: 7, computed:", find_kth_largest_builtin(arr, 3)) 

print(f"\n 1st largest elment in: {arr}: ")
print(f"expected: 9, computed:", find_kth_largest(arr, 1))
print(f"expected: 9, computed:", find_kth_largest_builtin(arr, 1)) 

print(f"\n 9th largest elment in: {arr}: ")
print(f"expected: 1, computed:", find_kth_largest(arr, 9))
print(f"expected: 1, computed:", find_kth_largest_builtin(arr, 9)) 