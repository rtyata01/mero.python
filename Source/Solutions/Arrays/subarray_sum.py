from collections import defaultdict

def subarray_sum(nums, k):
    count = 0
    prefix_sum = 0
    sum_freq = defaultdict(int)  # store the integer sum and its occurrence.
    sum_freq[0] = 1  # Base case: a sum of 0 has occurred once (empty subarray)

    for num in nums:
        prefix_sum += num
        count += sum_freq[prefix_sum - k]  # num[j] - num[j-1] = k, num[j-1] = num[j] - k
        sum_freq[prefix_sum] += 1

    return count

arr = [1, 2, 3]    
# {0:1} 
# {0:1, 1:1}
# {0:1, 1:1, 3:1}
# {0:1, 1:1, 3:1, 6:2}  # sum, count
print(f"expected: 2, result: ", subarray_sum(arr, 3))

arr = [1, 1, 1]    
print(f"expected: 2, result: ", subarray_sum(arr, 2))

arr = [1, -1, 0]   
print(f"expected: 3, result: ", subarray_sum(arr, 0))
