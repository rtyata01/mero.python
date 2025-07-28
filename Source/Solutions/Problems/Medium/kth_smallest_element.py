# Problem: Find the kth largest element in an unsorted array.


# 1. Using Sorting (simplest alternative)
# 2. Using a Min-Heap Manually (without heapq.nsmallest)
# 3. Using Quickselect (efficient for large lists)

import heapq

def find_kth_smallest_builtin(nums, k):
    return heapq.nsmallest(k, nums)[-1]

    # heapq.nsmallest(3, nums)  # → [2, 4, 7]
    # heapq.nsmallest(3, nums)[-1]  # → 7 (3rd smallest)

# Time Complexity: O(n log k) 
# Space Complexity: O(k)

def find_kth_smallest(arr, k):
    if not (1 <= k <= len(arr)):
        raise ValueError("k must be between 1 and the length of the list.")

    min_heap = arr[:]  # equivalent to arr.copy(), which creates a new array object with the same elements.
    heapq.heapify(min_heap)

    for _ in range(k - 1):
        heapq.heappop(min_heap)

    return min_heap[0]

# Time Complexity: O(n + k log n) 
# Space Complexity: O(k)

def find_kth_smallest_quickselect(nums, k):
    def quickselect(left, right, index):
        pivot = nums[right]
        p = left
        for i in range(left, right):
            if nums[i] <= pivot:  # note: <= for k-th smallest
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
        nums[p], nums[right] = nums[right], nums[p]

        if p == index:
            return nums[p]
        elif p < index:
            return quickselect(p + 1, right, index)
        else:
            return quickselect(left, p - 1, index)

    return quickselect(0, len(nums) - 1, k - 1)  # k-1 because index is 0-based

# Time Complexity	
    #   best = O(n)
    #   worst = O(n²)
# Space Complexity	
    #   best = O(log n)
    #   worst = O(n)

# Test
arr = [3, 2, 1, 5, 7, 8, 9, 6, 4]
print(f"\n 4th smallest elment in: {arr}: ")
print(f"expected: 4, computed:", find_kth_smallest(arr, 4))
print(f"expected: 4, computed:", find_kth_smallest_builtin(arr, 4)) 

print(f"\n 3rd smallest elment in: {arr}: ")
print(f"expected: 3, computed:", find_kth_smallest(arr, 3))
print(f"expected: 3, computed:", find_kth_smallest_builtin(arr, 3)) 

print(f"\n 1st smallest elment in: {arr}: ")
print(f"expected: 1, computed:", find_kth_smallest(arr, 1))
print(f"expected: 1, computed:", find_kth_smallest_builtin(arr, 1)) 

print(f"\n 9th smallest elment in: {arr}: ")
print(f"expected: 9, computed:", find_kth_smallest(arr, 9))
print(f"expected: 9, computed:", find_kth_smallest_builtin(arr, 9)) 