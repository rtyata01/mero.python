def unique_paths_with_obstacles(grid):
    if not grid or grid[0][0] == 1:
        return 0

    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                grid[i][j] = 0  # Obstacle, no paths through here
            elif i == 0 and j == 0:
                grid[i][j] = 1  # Start cell
            else:
                up = grid[i - 1][j] if i > 0 else 0
                left = grid[i][j - 1] if j > 0 else 0
                grid[i][j] = up + left

    return grid[-1][-1]

# 0 = free, 1 = obstacle
grid = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0]
]

print("Unique paths:", unique_paths_with_obstacles(grid))  # Output: 3

