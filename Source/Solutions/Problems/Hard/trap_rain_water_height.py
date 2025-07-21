# Hard: Compute total water trapped at a particular bar depends on the tallest bar to its left and tallest bar to its right. The trapped water at index i is:
# water_at_i = min(max_height_left, max_height_right) - height[i]

# Use two pointers: one at the start (left), one at the end (right).
# Keep track of the maximum height seen so far from the left (left_max) and from the right (right_max).
# Move the pointers inward, calculating trapped water as you go.

def trap(height):
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    trapped_water = 0
    
    while left < right:
        if height[left] < height[right]:
            left += 1   # incrementing first as left boundary cannot hold water.
            left_max = max(left_max, height[left])
            trapped_water += max(0, left_max - height[left])
        else:
            right -= 1 # decrementing first  as right boundary cannot hold water.
            right_max = max(right_max, height[right])
            trapped_water += max(0, right_max - height[right])
    
    return trapped_water

# Time Complexity: O (n)
# Space Complexity: O (1)

heights = [0,1,0]
print(f"Expected trapped water: 0, Computed trapped water: ", trap(heights))

heights = [3,0,2]  
# index 0 = 0 (no left boundary)
# index 1 = min(3, 2) - 0 = 2
# index 2 = 0 (no right boundary)
print(f"Expected trapped water: 2, Computed trapped water: ", trap(heights))

heights = [3,0,2,0,4] 
# index 0 = 0
# index 1 = min(3,4) - 0 = 3
# index 2 = min(3,4) - 2 = 1
# index 3 = min(3,4) - 0 = 3
# index 4 = 0
print(f"Expected trapped water: 7, Computed trapped water: ", trap(heights))

heights = [4, 2, 0, 3, 2, 5]
# index 0 = 0
# index 1 = min(4,5) - 2 = 2
# index 2 = min(4,5) - 0 = 4
# index 3 = min(4,5) - 3 = 1
# index 4 = min(4,5) - 2 = 2
# index 5 = 0
print(f"Expected trapped water: 9, Computed trapped water: ", trap(heights))
