
# Problem: Return the k most frequent elements in the list.

from collections import Counter
import heapq

def top_k_frequent(nums, k):
    count = Counter(nums)
    return [item for item, _ in heapq.nlargest(k, count.items(), key=lambda x: x[1])]


# count = {5: 3, 6: 1, 3: 2}  # Counter order reflects the order of first apperance.
# max_heap = [(5, 3), (3, 2), (6,1)] # max_heap of 2 = [(5, 3), (3,2)]
# 2 most frequent = [5, 3]

# Time Complexity: O(n + m log k)
# Counter = O(n)
# heap = O(m log k), where m is unique elements and k is the min heap size.

# Test 1 - Basic input with clear top frequency
print("Expected: [5, 3],", "Output:", top_k_frequent([5, 5, 5, 6, 3, 3], 2))

# Test 2 - All elements with same frequency
print("Expected: [1, 2],", "Output:", top_k_frequent([1, 2, 3, 4], 2))  # Any two of [1,2,3,4] valid

# Test 3 - Single element list
print("Expected: [5],", "Output:", top_k_frequent([5], 1))

# Test 4 - k equals length of unique elements
print("Expected: [1, 2, 3],", "Output:", top_k_frequent([1, 2, 3], 3))

# Test 5 - More frequent elements later in list
print("Expected: [3, 2],", "Output:", top_k_frequent([3, 3, 3, 2, 2, 1], 2))

# Test 6 - Negative numbers
print("Expected: [-1, -2],", "Output:", top_k_frequent([-1, -1, -1, -2, -2, -3], 2))

# Test 7 - Tie on frequency, check ordering doesn't matter
print("Expected: [1, 2],", "Output:", top_k_frequent([1, 2, 3, 1, 2, 3], 2))  # Any 2 of [1,2,3] valid

# Test 8 - Empty list
print("Expected: [],", "Output:", top_k_frequent([], 0))