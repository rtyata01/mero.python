# count all contiguous subarrays of length ≥ 3 where the elements form an arithmetic sequence.
# that is, the difference between consecutive elements is constant.

def count_arithmetic_subarrays(nums):
    n = len(nums)
    total = 0
    curr = 0  # Number of arithmetic subarrays ending at index i

    for i in range(2, n):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            curr += 1
            total += curr
        else:
            curr = 0  # Reset if the sequence breaks

    return total

def find_arithmetic_subarrays(nums):
    n = len(nums)
    result = []
    count = 0
    start = 0  # start of current potential arithmetic sequence

    for i in range(2, n):
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            # Continue the arithmetic sequence
            # For each extension, generate subarrays ending at i
            for j in range(start, i):
                if i + 1 - j >= 3:
                    new_array = nums[j:i+1]
                    result.append(nums[j:i+1])
                    count += 1
        else:
            # Sequence broken
            start = i - 1

    return result


nums = [1, 2, 3, 4]
# Valid arithmetic subarrays:
# [1,2,3], [2,3,4], [1,2,3,4]
print(f"Expected Output: 3, Arthmetic subarrays count: ", count_arithmetic_subarrays(nums))
print(f"Expected Output: 3, Arthmetic subarrays count: ", find_arithmetic_subarrays(nums))

nums = [7, 5, 3, 1, 2, 3, 4]
# Valid arithmetic subarrays:
# [1,2,3], [2,3,4], [1,2,3,4]
# [7,5,3], [5,3,1], [7,5,3,1]
print(f"Expected Output: 6, Arthmetic subarrays count: ", count_arithmetic_subarrays(nums))
print(f"Expected Output: 3, Arthmetic subarrays count: ", find_arithmetic_subarrays(nums))
