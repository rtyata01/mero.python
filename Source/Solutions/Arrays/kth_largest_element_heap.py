import heapq

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
    heapq.heapify(arr)  # Convert array into a min-heap
    for _ in range(k - 1):  # Pop k-1 smallest elements
        heapq.heappop(arr)
    return heapq.heappop(arr)  # The k-th smallest element

    # Time complexity: O(n + k log n) is generally better when k is large 

# Test
arr = [3, 2, 1, 5, 6, 4]
k = 4
print(f"\n{k} largest elment in: {arr}: ")
print(find_kth_largest(arr, k))  # Output: 4

print(f"\n{k} smallest elment in: {arr}: ")
print(find_kth_smallest(arr, k))  # Output: 4

print(f"\n{k} smallest elment in: {arr}: ")
print(find_kth_smallest_v2(arr, k))  # Output: 4
