def unique_paths_with_obstacles(grid):
    if not grid or grid[0][0] == 0:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                grid[i][j] = 0 # Set Obstacle statys 0
            elif i == 0 and j == 0:
                grid[i][j] = 1 # Set Starting point as 1
            else:
                up = grid[i-1][j] if i > 0 else 0
                left = grid[i][j-1] if j > 0 else 0
                grid[i][j] = up + left
    
    return grid[-1][-1]

# If the cell is free (not an obstacle), the number of paths to reach it is the sum of paths from
#    the cell above (if any), and
#    the cell to the left (if any).

# Time Complexity: O(m * n) time and O(1) space.

# 1 = free, 0 = obstacle
grid = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

print("Unique paths (right + down):", unique_paths_with_obstacles(grid))  # Output: 2

# 1 = free, 0 = obstacle
grid = [
    [1, 1, 1],
    [1, 0, 0],
    [1, 1, 1]
]

print("Unique paths (right + down):", unique_paths_with_obstacles(grid))  # Output: 1