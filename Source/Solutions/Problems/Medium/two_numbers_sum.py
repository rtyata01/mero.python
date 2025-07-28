# Problem: Given an array nums and a target sum, return indices of the two numbers that add up to the target.

# two_sum works for both positive and negative numbers. 
def two_sum(nums, target):
    seen = {}  # Maps number to its index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement] , i ] # 0-based indexing
        
        seen[num] = i

    return []  # If no solution is found

# Time Complexity: O (n)
# Space Complexity: O (n), worst case all elements stored in seen.

from collections import defaultdict
def all_two_sums(nums, target):
    
    seen = defaultdict(list)  # Maps number to list of indices
    result = []

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            for j in seen[complement]:
                result.append([j, i])
        seen[num].append(i)

    return result

# twoSum works only for sorted positive integers, but not for negative numbers.
def twoSum(numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target:
            return [left , right ]  # 0-based indexing [left +1, right + 1] 1-based indexing
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []

# Time Complexity: O (n)
# Space Complexity: O (1)


# Tests
print(f"Expected Output: [],             Result: ", all_two_sums([2,3,7,11,15], 9))
print(f"Expected Output: [],             Result: ", all_two_sums([], 5))
print(f"Expected Output: [],             Result: ", all_two_sums([3], 3))
print(f"Expected Output: [],             Result: ", all_two_sums([1, 2, 3], 7))
print(f"Expected Output: [1, 2],         Result: ", all_two_sums([1, 2, 3, 4], 5))  # Could also be [0, 3]
print(f"Expected Output: [0, 1],         Result: ", all_two_sums([3, 3], 6))
print(f"Expected Output: [2, 4],         Result: ", all_two_sums([-1, -2, -3, -4, -5], -8))
print(f"Expected Output: [0, 3],         Result: ", all_two_sums([0, 4, 3, 0], 0))
print(f"Expected Output: [999998, 999999], Result: ", all_two_sums(list(range(1, 10**6)), 1999999))


print(f"Expected Output: [],             Result: ", twoSum([2,3,7,11,15], 9))
print(f"Expected Output: [],             Result: ", twoSum([], 5))
print(f"Expected Output: [],             Result: ", twoSum([3], 3))
print(f"Expected Output: [],             Result: ", twoSum([1, 2, 3], 7))
print(f"Expected Output: [1, 2],         Result: ", twoSum([1, 2, 3, 4], 5))  # Could also be [0, 3]
print(f"Expected Output: [0, 1],         Result: ", twoSum([3, 3], 6))
print(f"Expected Output: [2, 4],         Result: ", twoSum([-1, -2, -3, -4, -5], -8))
print(f"Expected Output: [0, 3],         Result: ", twoSum([0, 4, 3, 0], 0))
print(f"Expected Output: [999998, 999999], Result: ", twoSum(list(range(1, 10**6)), 1999999))