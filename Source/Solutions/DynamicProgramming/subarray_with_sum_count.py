from collections import defaultdict

def subarray_sum(nums, target_sum):
    count = 0
    prefix_sum = 0
    sum_freq = defaultdict(int)  # store the integer sum and its occurrence.
    sum_freq[0] = 1  # Base case: a sum of 0 has occurred once (empty subarray)

    for num in nums:
        prefix_sum += num
        count += sum_freq[prefix_sum - target_sum]  # num[j] - num[j-1] = k, num[j-1] = num[j] - k
        sum_freq[prefix_sum] += 1

    return count

# Time Complexity:  O(n) - Single pass through the array
# Space	Complexity: O(n) - Stores prefix sums in hashmap

# Tests
test_cases = [
    ([1, 2, 3], 15),
    ([1, 2, 3], 3),
    ([1, 1, 1], 2),
    ([1, -1, 0], 0),
    ([1, -1, 0, -2 , 2], 0),
]

for arr, target_sum in test_cases:
    result = subarray_sum(arr, target_sum)
    print(f"Input: {arr} and sum: {target_sum}, subarray count: {result}")

# Input: ([1, 2, 3], 3)
# {0:1} 
# {0:1, 1:1}
# {0:1, 1:1, 3:1}
# {0:1, 1:1, 3:2}  # sum, count
# sum=3, count=2

# ([1, -1, 0], 0),
# sum=0, count=3, [1, -1], [0], [1, -1, 0]