# Hard: Compute total trapped water. 
# The trapped water at index i is: dependes upon the tallest bar to its left and tallest bar to its right. 

# For naive and less efficient approach
    # water_at_index = min(max_left, max_right) - height[i]
    
# Efficient approach, Use two pointers: one at the start (left), one at the end (right).
    # trapped water = min(0, max_left - height[left]) from left.
    # trapped water = min(0, max_right - height[right]) from right.
# Keep track of the maximum height seen so far from the left (left_max) and from the right (right_max).
# Move the pointers inward, calculating trapped water as you go.
# Left and Right boundary will not collect any water.

def find_trapped_water(height):
    if not height:
        return 0
    
    left = 0 
    right = len(height) - 1
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

def find_trapped_water_naive(height):
    n = len(height)
    trapped_water = 0
    
    for i in range(n):
        left_max = max(height[:i+1])     # scan left from 0 to i
        right_max = max(height[i:])      # scan right from i to end
        water = min(left_max, right_max) - height[i]
        if water > 0:
            trapped_water += water
    
    return trapped_water

# Time Complexity: O (n^2)
# Space Complexity: O (1)

heights = [0,1,0]
print(f"Expected trapped water: 0, Computed trapped water: ", find_trapped_water(heights))

heights = [3,0,2]  
# index 0 = 0 (no left boundary)
# index 1 = min(3, 2) - 0 = 2
# index 2 = 0 (no right boundary)
print(f"Expected trapped water: 2, Computed trapped water: ", find_trapped_water(heights))

heights = [3,0,2,0,4] 
print(f"Expected trapped water: 7, Computed trapped water: ", find_trapped_water(heights))

heights = [4, 2, 6, 3, 2, 5]
print(f"Expected trapped water: 7, Computed trapped water: ", find_trapped_water(heights))
