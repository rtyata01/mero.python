from collections import defaultdict

def subarray_sum_with_tracking(nums, k):
    prefix_sum = 0
    count = 0
    result = []  # Stores the actual subarrays
    sum_indices = defaultdict(list)
    sum_indices[0].append(-1)  # Base case for subarrays starting at index 0  

    for i, num in enumerate(nums):
        prefix_sum += num

        # Check if there's any subarray ending at i with sum = k
        if (prefix_sum - k) in sum_indices:
            for start_index in sum_indices[prefix_sum - k]:
                subarray = nums[start_index + 1: i + 1]
                result.append(subarray)
                count += 1

        sum_indices[prefix_sum].append(i)

    return count, result


arr = [1, 2, 3]
# {0: [-1]}
# {0: [-1], 1: [0]}
# {0: [-1], 1: [0], 3: [1]}
# {0: [-1], 1: [0], 3: [1], 6: [2]}  # sum and ending index
count, result = subarray_sum_with_tracking(arr, 3)
print(f"expected: 2, count: {count} and result: {result}")

arr = [1, 1, 1]
count, result = subarray_sum_with_tracking(arr, 3)
print(f"expected: 2, count: {count} and result: {result}")

arr = [1, -1, 0]   
count, result = subarray_sum_with_tracking(arr, 0)
print(f"expected: 3, count: {count} and result: {result}")
