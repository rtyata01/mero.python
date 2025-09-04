import heapq

def find_kth_nlargest(nums, k):
    return heapq.nlargest(k, nums)[-1]  # [5, 4, 3] # result[-1] = 3

def find_kth_nsmallest(nums, k):
    return heapq.nsmallest(k, nums)[-1]  # [1, 2] # result[-1] = 2

def find_kth_largest(nums, k):
    min_heap = nums[:k]
    heapq.heapify(min_heap) # list is rearranged into a valid min-heap tree, where parent nodes is smaller than 2 child nodes.
    
    for num in nums[k:]:
        if num > min_heap[0]:  # If current element is larger than the smallest in heap
            heapq.heappop(min_heap) # remove smallest element from min heap, located at position 0.
            heapq.heappush(min_heap, num)
    
    return min_heap[0]

    # Time complexity: = O(n log k) = O(k) (heapify) + O((n−k)⋅logk) 

def find_kth_smallest(nums, k):
    max_heap = [-num for num in nums[:k]]  # Negate to simulate max-heap, as python only have min heap.
    heapq.heapify(max_heap)
    
    for num in nums[k:]:
        if -num > max_heap[0]:  # If the current element is smaller than the largest in the heap
            heapq.heappop(max_heap)  # Remove the largest element (root of the max-heap)
            heapq.heappush(max_heap, -num)  # Push the new element (negate to maintain max-heap)
    
    return -max_heap[0]
    # Time complexity: O(n log k) is better for small k, 

def find_kth_smallest_v2(arr, k):
    if not 1 <= k <= len(arr):
        raise ValueError("k must be between 1 and the length of the list.")

    min_heap = arr[:]  # equivalent to arr.copy(), which creates a new array object with the same elements.
    heapq.heapify(min_heap)

    for _ in range(k - 1):
        heapq.heappop(min_heap)

    return min_heap[0]

# Test
arr = [3, 2, 1, 5, 7, 8, 9, 6, 4]
k = 4
print(f"\n{k} largest elment in: {arr}: ")
print(find_kth_largest(arr, k))  # Output: 4

print(f"\n{k} smallest elment in: {arr}: ")
print(find_kth_smallest(arr, k))  # Output: 4

print(f"\n{k} smallest elment in: {arr}: ")
print(find_kth_smallest_v2(arr, k))  # Output: 4
