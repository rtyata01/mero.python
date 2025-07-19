# Problem: Find the kth largest element in an unsorted array.

import heapq

def find_kth_smallest_builtin(nums, k):
    return heapq.nsmallest(k, nums)[-1]

    # heapq.nsmallest(3, nums)  # → [2, 4, 7]
    # heapq.nsmallest(3, nums)[-1]  # → 7 (3rd smallest)

# Time Complexity: O(n log k) 
# Space Complexity: O(k)

def find_kth_smallest(arr, k):
    if not 1 <= k <= len(arr):
        raise ValueError("k must be between 1 and the length of the list.")

    min_heap = arr[:]  # equivalent to arr.copy(), which creates a new array object with the same elements.
    heapq.heapify(min_heap)

    for _ in range(k - 1):
        heapq.heappop(min_heap)

    return min_heap[0]

# Time Complexity: O(n + k log n) 
# Space Complexity: O(k)

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