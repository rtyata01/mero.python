# Hard: Given an array arr and a window size k, find the minimum element in each contiguous subarray of size k.
# Find the min in each window of size k and use queue for implementation.
# Remove indices from the front queue, when the window size is bigger.
# Remove values from the back of the queue, when new element is smaller.

from collections import deque

def min_sliding_window(arr, window_size):
    if not arr or window_size == 0:
        return []

    queue = deque()  # will store indices
    results = []

    for i in range(len(arr)):
        # Remove indices that are out of the current window
        while queue and queue[0] < i - window_size + 1:
            queue.popleft()

        # Remove elements larger than the current one from the back of the queue
        while queue and arr[queue[-1]] > arr[i]:
            queue.pop()

        queue.append(i)

        # Append the min value once the first window is full
        if i >= window_size - 1:
            results.append(arr[queue[0]])

    return results

# Time Complexity: O(n)
# Space Complexity: O(k) queue + O(n - k + 1) store in results.         


# without using queue
def man_in_sliding_window_naive_less_efficient(arr, k):
    if not arr or k == 0:
        return []
    
    result = []
    for i in range(len(arr) - k + 1):
        result.append(min(arr[i:i + k]))

    return result

# Time Complexity: O(n * k) where n is the length of the array.
                                                                                                                    

# Example usage:
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(min_sliding_window(arr, k))  # Output: [-1, -3, -3, -3, 3, 3]
print(man_in_sliding_window_naive_less_efficient(arr, k))

# Example usage:
arr = [1, 3, -1, -2, -3, 5, 3, 6, 7]
k = 3
print(min_sliding_window(arr, k))  # Output: [-1, -2, -3, -3, -3, 3, 3] 
print(man_in_sliding_window_naive_less_efficient(arr, k))

