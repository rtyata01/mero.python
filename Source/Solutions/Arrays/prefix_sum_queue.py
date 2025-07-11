# Shortest Subarray with Sum at Least K

# Approach Handles      Negatives?	Time Complexity	Recommended?
# Sliding window	    No	        O(n)	        Only for all positive
# Prefix sum + deque	Yes	        O(n)	        Yes, always
# Brute force	        Yes	        O(n²)	        For small inputs

from collections import deque

def shortest_subarray(nums, k):
    n = len(nums)
    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    dq = deque()
    min_len = n + 1
    start_idx = -1

    for i in range(n + 1):
         # Check if current prefix sum - earliest prefix sum in deque >= k
        while dq and prefix[i] - prefix[dq[0]] >= k:
            j = dq.popleft()
            if i - j < min_len:
                min_len = i - j
                start_idx = j

        # Maintain deque increasing order of prefix sums
        while dq and prefix[i] <= prefix[dq[-1]]:
            dq.pop()

        dq.append(i)

    if min_len <= n:
        subarray = nums[start_idx:start_idx + min_len]
        return min_len, subarray
    else:
        return -1, []


nums = [1, 2, 3, 4, 5]
k = 11
length, subarray = shortest_subarray(nums, k)
print("Length:", length)
print("Subarray:", subarray)


nums = [1, -1, 5, 2, 3, 4, 3, 2]
k = 8
length, subarray = shortest_subarray(nums, k)
print("Length:", length)
print("Subarray:", subarray)

#i	prefix[i]	dq (before)	Operation	Updated dq	    Found Subarray?
#0	0	        []	        append      0	    [0]	    ❌
#1	1	        [0]	        append      1	    [0, 1]	❌
#2	0	        [0,1]	    pop         1,0	    [2]	    ❌
#3	5	        [2]	        append      3	    [2,3]	❌
#4	7	        [2,3]	    append      4	    [2,3,4]	❌
#5	10	        [2,3,4]	    pop         2	    [3,4,5]	✅  [5,2,3]
#6	14	        [3,4,5]	    pop         3	    [4,5,6]	✅  [2,3,4]
#7	17	        [4,5,6]	    pop         4	    [5,6,7]	✅  [3,4,3]
#8	19	        [5,6,7]	    pop         5	    [6,7,8]	✅  [4,3,2]