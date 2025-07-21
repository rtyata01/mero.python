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

# twoSum works only for sorted positive integers, but not for negative numbers.
def twoSum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
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
print(f"Expected Output: [],             Result: ", two_sum([2,3,7,11,15], 9))
print(f"Expected Output: [],             Result: ", two_sum([], 5))
print(f"Expected Output: [],             Result: ", two_sum([3], 3))
print(f"Expected Output: [],             Result: ", two_sum([1, 2, 3], 7))
print(f"Expected Output: [1, 2],         Result: ", two_sum([1, 2, 3, 4], 5))  # Could also be [0, 3]
print(f"Expected Output: [0, 1],         Result: ", two_sum([3, 3], 6))
print(f"Expected Output: [2, 4],         Result: ", two_sum([-1, -2, -3, -4, -5], -8))
print(f"Expected Output: [0, 3],         Result: ", two_sum([0, 4, 3, 0], 0))
print(f"Expected Output: [999998, 999999], Result: ", two_sum(list(range(1, 10**6)), 1999999))


print(f"Expected Output: [],             Result: ", twoSum([2,3,7,11,15], 9))
print(f"Expected Output: [],             Result: ", twoSum([], 5))
print(f"Expected Output: [],             Result: ", twoSum([3], 3))
print(f"Expected Output: [],             Result: ", twoSum([1, 2, 3], 7))
print(f"Expected Output: [1, 2],         Result: ", twoSum([1, 2, 3, 4], 5))  # Could also be [0, 3]
print(f"Expected Output: [0, 1],         Result: ", twoSum([3, 3], 6))
print(f"Expected Output: [2, 4],         Result: ", twoSum([-1, -2, -3, -4, -5], -8))
print(f"Expected Output: [0, 3],         Result: ", twoSum([0, 4, 3, 0], 0))
print(f"Expected Output: [999998, 999999], Result: ", twoSum(list(range(1, 10**6)), 1999999))