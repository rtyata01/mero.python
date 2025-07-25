# Hard: Given an array arr and a window size k, find the maximum element in each contiguous subarray of size k.
# Find the max in each window of size k and use queue for implementation.
# Remove indices from the front queue, when the window size is bigger.
# Remove values from the back of the queue, when new element is higher.

from collections import deque

def max_sliding_window(arr, window_size):
    if not arr or window_size == 0:
        return []

    queue = deque()  # will store indices
    results = []

    for i in range(len(arr)):
        # Remove elements out of the window i.e. from front of the queue
        while queue and queue[0] < i - window_size + 1:
            queue.popleft()

        # Remove elements smaller than current from the back of the queue.
        while queue and arr[queue[-1]] < arr[i]:
            queue.pop()

        queue.append(i)

        # Append max value to result once we have the first full window
        if i >= window_size - 1:
            results.append(arr[queue[0]])

    return results

# Time Complexity: O(n)
# Space Complexity: O(k) queue + O(n - k + 1) store in results.                                                                                                                             

# without using queue
def max_in_sliding_window_naive_less_efficient(arr, k):
    if not arr or k == 0:
        return []
    
    result = []
    for i in range(len(arr) - k + 1):
        result.append(max(arr[i:i + k]))

    return result

# Time Complexity: O(n * k) where n is the length of the array.

# Example usage:
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(max_sliding_window(arr, k))  # Output: [3, 3, 5, 5, 6, 7]
print(max_in_sliding_window_naive_less_efficient(arr, k))
# i = 0, queue = [0],       result = []
# i = 1, queue = [1],       result = []
# i = 2, queue = [1,2],     result = [3]
# i = 3, queue = [1,2,3],   result = [3, 3]
# i = 4, queue = [4],       result = [3, 3, 5]
# i = 5, queue = [4,5],     result = [3, 3, 5, 5]
# i = 6, queue = [6],       result = [3, 3, 5, 5, 6]
# i = 7, queue = [7],       result = [3, 3, 5, 5, 6, 7]

# Example usage:
arr = [1, 3, -1, -2, -3, 5, 3, 6, 7]
k = 3
print(max_sliding_window(arr, k))  # Output: [3, 3, 5, 5, 6, 7]
print(max_in_sliding_window_naive_less_efficient(arr, k))
# i = 0, queue = [0],       result = []
