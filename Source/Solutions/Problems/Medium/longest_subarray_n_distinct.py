# Given an array of integers, find the length of the longest subarray with at most N distinct numbers.

from collections import defaultdict
def longest_subarray_n_distinct(nums, unique_numbers):
    if not nums:
        return []
    
    count = defaultdict(int)
    max_length = 0
    left = 0
    result = []
    
    for right, num in enumerate(nums):
        count[num] +=1
        
        while len(count) > unique_numbers:
            left_num = nums[left]
            if count[left_num] > 1:
                count[left_num] -=1
            else:
                del count[left_num]
            left +=1
        
        if right - left + 1 > max_length:
            max_length = right - left + 1
            result = nums[left: right + 1]
            
    return result

nums = [1, 2, 1, 2, 3, 2, 2, 1, 4]
result = longest_subarray_n_distinct(nums, 2)
print(f"longest subarray with [2] unique element is: {result} with length: {len(result)}")

result = longest_subarray_n_distinct(nums, 3)
print(f"longest subarray with [3] unique element is: {result} with length: {len(result)}")

result = longest_subarray_n_distinct(nums, 4)
print(f"longest subarray with [4] unique element is: {result} with length: {len(result)}")

nums = []
result = longest_subarray_n_distinct(nums, 2)
print(f"longest subarray with [2] unique element is: {result} with length: {len(result)}")

nums = [1, 1, 1]
result = longest_subarray_n_distinct(nums, 2)
print(f"longest subarray with [2] unique element is: {result} with length: {len(result)}")