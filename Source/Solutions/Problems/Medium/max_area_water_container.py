# Given an array of heights representing vertical lines, find two lines that form a container with the maximum water volume.
# Water area at each cell.
    # area = min(height[left], height[right]) * (right - left)

def maxArea(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

# Time Complexity: O(n)
# Space Complexity: O(1)

# naive, brute force approach, less efficient.
def maxAreaNaive(height: list[int]) -> int:
    max_water = 0
    n = len(height)
    for i in range(n):
        for j in range(i + 1, n):
            area = min(height[i], height[j]) * (j - i)
            max_water = max(max_water, area)
    return max_water

# Time Complexity: O(n^2)

# Tests
nums = [1, 8, 6, 2, 5]
# left=0,right=4, area = min(1,5) * (4 - 0) = 1 * 4 = 4
# left=1,right=4, area = min(8,5) * (4 - 1) = 5 * 3 = 15 (max)
# left=1,right=3, area = min(8,2) * (3 - 1) = 2 * 2 = 4
print(f"Input: {nums}, max area of water container: {maxArea(nums)}")

nums = []
print(f"Input: {nums}, max area of water container: {maxArea(nums)}")

nums = [5]
print(f"Input: {nums}, max area of water container: {maxArea(nums)}")

nums = [1, 1]
print(f"Input: {nums}, max area of water container: {maxArea(nums)}")

nums = [1, 2]
print(f"Input: {nums}, max area of water container: {maxArea(nums)}")

nums = [2, 1]
print(f"Input: {nums}, max area of water container: {maxArea(nums)}")

nums = [1, 2, 4, 3]
print(f"Input: {nums}, max area of water container: {maxArea(nums)}")

nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(f"Input: {nums}, max area of water container: {maxArea(nums)}")

nums = [10000, 1, 10000]
print(f"Input: {nums}, max area of water container: {maxArea(nums)}")

nums = [2,1,5,6,2,3]
print(f"Input: {nums}, max area of water container: {maxArea(nums)}")