# Given an array of integers heights[] representing the heights of bars in a histogram (each bar is 1 unit wide),
# Return the area of the largest rectangle that can be formed in the histogram.

# Use Bruteforce, try all pairs of bars and compute height * width, which is O(n^2)
# Use stack to store the increasing heights, o(n)

def largest_rectangle_area(heights):
    if not heights:
        return None
    
    # Add a sentinel value to handle remaining stack elements 
    heights.append(0)  
    stack = []
    max_area = 0

    for i, h in enumerate(heights):
        # Ensure stack is increasing
        while stack and heights[stack[-1]] > h:
            top = stack.pop()
            height = heights[top]
            
            # If stack is empty, width = i
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
            
        stack.append(i)

    return max_area

# Tests
nums = [1, 2, 3, 4, 5]
print(f"Input: {nums}, largest rectangle area: {largest_rectangle_area(nums)}") 
# At height 5, width=1 from 5, area=5
# At height 4, width=2 from 5, area=8
# At height 3, width=3 from 5, area=9
# At height 2, width=4 from 5, area=8
# At height 1, width=5 from 5, area=5

nums = [5, 4, 3, 2, 1]
print(f"Input: {nums}, largest rectangle area: {largest_rectangle_area(nums)}")

nums = [1, 8, 6, 2, 5]
# nums = [1, 8, 6, 2, 5, 0] after appending 0.
# i=0,h=1, stack = [0]
# i=1,h=8, stack = [0, 1] stack[-1] 0 i.e. heights[0]> h = 1 > 8 false
# i=2,h=6 
    # stack = [0], 8 > 6 true, top=1, height=8, width=2-0-1=1, area=8
    # stack = [0, 2]
# i=3,h=2,  
    # stack = [0], 6 > 2 true, top=2, height=6, width=3-0-1=2, area=12
    # stack = [0, 3]
# i=4,h=5
    # h[3] 2 > 5 false.
    # stack = [0, 3, 4]
# i=5,h=0
    # h[4] 5 > 0, true
    # stack [0,3], top=4, height=5, width=5-3-1=1, area=5
    # stack [0], top=3, height=2, width=5-0-1=4, area=8
    # top=1, height=1, width=5, area=8
    # stack [5]

print(f"Input: {nums}, largest rectangle area: {largest_rectangle_area(nums)}")

nums = []
print(f"Input: {nums}, largest rectangle area: {largest_rectangle_area(nums)}")

nums = [5]
print(f"Input: {nums}, largest rectangle area: {largest_rectangle_area(nums)}")

nums = [5, 5, 5, 5]
print(f"Input: {nums}, largest rectangle area: {largest_rectangle_area(nums)}")


nums = [2, 0, 2]
print(f"Input: {nums}, largest rectangle area: {largest_rectangle_area(nums)}")

nums = [2, 10, 2, 10, 2]
print(f"Input: {nums}, largest rectangle area: {largest_rectangle_area(nums)}")
