
# Problem: Return the k most frequent elements in the list.

from collections import Counter
import heapq

def top_k_frequent(nums, k):
    count = Counter(nums) # {'a': 3, 'b': 5, 'c': 2}
    return [item for item, _ in heapq.nlargest(k, count.items(), key=lambda x: x[1])]  # heap [('b', 5), ('a', 3)], return # ['b', 'a']

def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)  # {'a': 3, 'b': 5, 'c': 2}
    return heapq.nlargest(k, count.keys(), key=count.get) # ['b', 'a']

def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)    # → Counter({1: 3, 3: 1, 2: 2}), nums = [1,1,1,3,2,2]
    sorted_items = sorted(count.items(), key=lambda item: item[1], reverse=True)  # [(1, 3), (2, 2), (3, 1)] # reverse=False, [(3, 1), (2, 2), (1, 3)]
    top_k = list(dict(sorted_items).keys())[:k]
    return top_k

def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    min_heap = []

    for num, freq in count.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [num for freq, num in min_heap]


def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)  # → Counter({1: 3, 3: 1, 2: 2}), nums = [1,1,1,3,2,2]
    freq_bucket = [[] for _ in range(len(nums) + 1)] # [[], [], [], [], [], [], []]
    
    for num, freq in count.items():    # highest frequecy will appear at higher index. [[], [3], [2], [1], [], [], []]
        freq_bucket[freq].append(num)
    
    result = []
    for i in range(len(freq_bucket) - 1, 0, -1):
        for num in freq_bucket[i]:
            result.append(num)
            if len(result) == k:
                return result

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