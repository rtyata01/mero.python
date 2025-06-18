def min_path_weight(grid):
    if not grid or grid[0][0] == -1:
        return -1

    rows, cols = len(grid), len(grid[0])
    INF = float('inf')

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == -1:
                grid[i][j] = INF # obstacle
            elif i == 0 and j == 0:
                continue  # start cell
            else:
                up = grid[i - 1][j] if i > 0 else INF
                left = grid[i][j - 1] if j > 0 else INF
                min_prev = min(up, left)
                grid[i][j] = grid[i][j] + min_prev if min_prev != INF else INF

    return grid[-1][-1] if grid[-1][-1] != INF else -1


# obstacles = -1, positive number = weight.

grid = [
    [1, 3, 1, 2],
    [1, -1, -1, 3],
    [2, 1, -1, 1],
    [4, 2, 1, 1]
]

print("Exprected: 9, Minimum weight path (2 directions):", min_path_weight(grid))  # Output: 9

grid = [
    [1, 3, 1, 2],
    [1, 1, -1, 3],
    [2, 1, 1, -1],
    [4, 2, 1, 1]
]

print("Exprected: 7, Minimum weight path (2 directions):", min_path_weight(grid))  # Output: 9