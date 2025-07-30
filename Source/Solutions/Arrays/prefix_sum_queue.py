# Find the shortest Subarray with Sum at Least K.

# Approach Handles      Negatives?	Time Complexity	Recommended?
# Sliding window	    No	        O(n)	        Only for all positive
# Prefix sum + deque	Yes	        O(n)	        Yes, always
# Brute force	        Yes	        O(n²)	        For small inputs

# Use prefix sum, calculate subarray sums in constant time by subtracting two prefix sums.
# Use double ended queue, store indices of prefix sums, such that prefix sums are in increasing order.

from collections import deque

def shortest_subarray(nums, k):
    n = len(nums)
    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    queue = deque()
    min_len = n + 1
    min_start_index = -1

    for i in range(n + 1):
         # Check if current prefix sum - earliest prefix sum in deque >= k
        while queue and prefix[i] - prefix[queue[0]] >= k:
            j = queue.popleft()
            current_length = i - j
            if current_length < min_len:
                min_len = current_length
                min_start_index = j

        # Maintain deque increasing order of prefix sums
        while queue and prefix[i] <= prefix[queue[-1]]:
            queue.pop()

        queue.append(i)

    if min_len <= n:
        subarray = nums[min_start_index:min_start_index + min_len]
        return min_len, subarray
    else:
        return -1, []

# Time Complexity: O(n)
# Space Complexity: O(n)

def shortest_subarray_bruteforce(nums, k):
    n = len(nums)
    min_len = n + 1
    start_idx = -1

    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total >= k:
                current_len = j - i + 1
                if current_len < min_len:
                    min_len = current_len
                    start_idx = i
                break  # No need to extend this subarray further

    if min_len <= n:
        return min_len, nums[start_idx:start_idx + min_len]
    else:
        return -1, []
    
# Time Complexity: O(n^2)
# Space Complexity: O(1)


nums = [1, 2, 3, 4, 5]
k = 11
# prefix sum =  [0, 1, 3, 6, 10, 15]
# i=0, queue=[0]
# i=1, queue=[0,1] prefix[1]-prefix[0] >= k i.e. 1-0 >= k false
# i=2, queue=[0,1,2] prefix[2]-prefix[0] >= k i.e. 3-0 >= k false
# i=3, queue=[0,1,2,3] prefix[3]-prefix[0] >= k i.e. 6-0 >= k false
# i=4, queue=[0,1,2,3,4] prefix[4]-prefix[0] >= k i.e. 10-0 >= k false
# i=5, queue=[0,1,2,3,4] prefix[5]-prefix[0] >= k i.e. 15-0 >= k true
    #  queue=[1,2,3,4] prefix[5]-prefix[1] >= k i.e. 15-1 >= k true
    #  queue=[2,3,4] prefix[5]-prefix[2] >= k i.e. 15-3 >= k true
    #  queue=[3,4] prefix[5]-prefix[3] >= k i.e. 15-6 >= k false
# shortest length = 3, start_index = 2 and end_index = 5
length, subarray = shortest_subarray(nums, k)
print("Length:", length)
print("Subarray:", subarray)

nums = [1, -1, 5, -2, 3, 4, 3]
k = 8
length, subarray = shortest_subarray(nums, k)
print("Length:", length)
print("Subarray:", subarray)
# prefix sum = [0, 1, 0, 5, 3, 6, 10]
# i=0, queue=[0]
# i=1, queue=[0,1] 
# i=2, queue=[0,1] prefix[1] <= prefix[2], 
    # queue[0], prefix[0] <= prefix[2]
    # queue[2]
# i=3, queue=[2,3] 
# i=4, queue=[2,3] prefix[3] <= prefix[4]
    # queue[2,4]
# i=5, queue=[2,4,5]
# i=6, queue=[2,4,5], prefix[6]-prefix[2] = 10-0 > 8
    # queue=[4,5] prefix[6]-prefix[4] >= k i.e. 10-3 >= k false
    # shortest length = 4, start_index = 2 and end_index = 6
    # queue=[4,5,6]
# i=7, queue=[4,5,6], prefix[7]-prefix[4] = 13-3 > 8
    # queue=[5,6] prefix[7]-prefix[5] >= k i.e. 13-6 >= k 
    # shortest length = 3, start_index = 4 and end_index = 7
    # queue=[5,6,7]
