# Problem: Given an array nums, return an array where each element is the product of all numbers except the one at that index, without using division.

def productExceptSelf(nums: list[int]) -> list[int]:
    if not nums or len(nums) < 2:
        raise ValueError("Input array must have at least 2 elements")
    
    n = len(nums)
    result = [1] * n
    
    # Left products
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]
        
    # Right products and combine
    right_product = 1
    for i in range(n-1, -1, -1):   # start at n-1, stop at -1, decrement by -1
        result[i] *= right_product
        right_product *= nums[i]
    return result

# Time Complexity: O(n)
# Space Complexity: O(1) (excluding output array)

# Tests
nums = [1, 5, 10]
print(f"Input: {nums}, Output: {productExceptSelf(nums)}") # output [50, 10, 5]

nums = [5, 10]
print(f"Input: {nums}, Output: {productExceptSelf(nums)}") # output [10, 5]

nums = [1]
print(f"Input: {nums}, Output: Error or [] (not enough elements)")

nums = [1, 1, 1, 1]
print(f"Input: {nums}, Output: {productExceptSelf(nums)}") # output [1, 1, 1, 1]

nums = [1, 2, 0, 4]
print(f"Input: {nums}, Output: {productExceptSelf(nums)}") # output [0, 0, 8, 0]

nums = [-1, 2, -3, 4]
print(f"Input: {nums}, Output: {productExceptSelf(nums)}") # output [-24, 12, -8, 6]

nums = [-1, 0, -3, 4]
print(f"Input: {nums}, Output: {productExceptSelf(nums)}") # output: [0, 12, 0, 0]