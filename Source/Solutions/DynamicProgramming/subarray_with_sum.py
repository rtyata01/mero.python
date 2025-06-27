# Count how many contiguous subarrays of nums, whose sum is exactly equal to k.
# Works with negative number as well.

from collections import defaultdict

def find_subarrays_with_sum(nums, target):
    current_sum = 0
    count = 0
    result = []
    sum_index = defaultdict(list)
    sum_index[0].append(-1)  # Handles subarrays starting from index 0

    for i, num in enumerate(nums):
        current_sum += num
        needed_sum = current_sum - target
        
        if needed_sum in sum_index:
            for start in sum_index.get(needed_sum, []):
                result.append(nums[start + 1:i + 1])
                count += 1

        sum_index[current_sum].append(i)

    return count, result

arr = [1, -1, 0, -2 , 2]
# {0: [-1]}

# i=0, num=1,  {0: [-1], 1: [0]}
# i=1, num=-1, {0: [-1, 1], 1: [0]}                     # [1, -1],
# i=2, num=0,  {0: [-1, 1, 2], 1: [0]}                  # [1, -1, 0], [0]
# i=3  num=-2, {0: [-1, 1, 2], 1: [0], -2: [3]}         
# i=4  num=2,  {0: [-1, 1, 2], 1: [0], 2: [4]} sum and ending index   # [1, -1, 0, -2, 2], [0, -2, 2], [-2, 2]
count, result = find_subarrays_with_sum(arr, 0)
print(f"expected subarray count: 6, count: {count} and result: {result}")

arr = [1, 2, 3]
# {0: [-1]}

# i=0, num=1, {0: [-1], 1: [0]}
# i=1, num=2, {0: [-1], 1: [0], 3: [1]}
# i=2, num=3, {0: [-1], 1: [0], 3: [1], 6: [2]}  # sum and ending index
count, result = find_subarrays_with_sum(arr, 3)
print(f"expected subarray count: 2, count: {count} and result: {result}")

arr = [1, 1, 1]
# {0: [-1]}

# i=0, num=1, {0: [-1], 1: [0]}
# i=1, num=1, {0: [-1], 1: [0], 2: [1]}
# i=2, num=1, {0: [-1], 1: [0], 2: [1, 2]}  # sum and ending index
count, result = find_subarrays_with_sum(arr, 2)
print(f"expected subarray count: 2, count: {count} and result: {result}")


