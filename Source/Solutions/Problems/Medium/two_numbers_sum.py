# Problem: Given an array nums and a target sum, return indices of the two numbers that add up to the target.

def two_sum(nums, target):
    seen = {}  # Maps number to its index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []  # If no solution is found

# Time Complexity: O (n)
# Space Complexity: O (n), worst case all elements stored in seen.

# Tests
print(f"Expected Output: [],             Result: ", two_sum([], 5))
print(f"Expected Output: [],             Result: ", two_sum([3], 3))
print(f"Expected Output: [],             Result: ", two_sum([1, 2, 3], 7))
print(f"Expected Output: [1, 2],         Result: ", two_sum([1, 2, 3, 4], 5))  # Could also be [0, 3]
print(f"Expected Output: [0, 1],         Result: ", two_sum([3, 3], 6))
print(f"Expected Output: [2, 4],         Result: ", two_sum([-1, -2, -3, -4, -5], -8))
print(f"Expected Output: [0, 3],         Result: ", two_sum([0, 4, 3, 0], 0))
print(f"Expected Output: [999998, 999999], Result: ", two_sum(list(range(1, 10**6)), 1999999))