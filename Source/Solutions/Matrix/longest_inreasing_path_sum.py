def find_longest_increasing_path(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    directions = [(-1 , 0), (1 , 0), (0, -1), (0, 1)] # up, down, left, right
    # directions  += [(-1, -1), (-1, 1), (1, -1), (1, 1)] # diagonal traversal
    max_path = 0

    def dfs(x, y, visited):
        max_len = 0
        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited) and grid[nx][ny] > grid[x][y]:
                max_len = max(max_len, dfs(nx, ny, visited))

        visited.remove((x, y))  # Backtrack
        return max_len + grid[x][y] 

    for i in range(rows):
        for j in range(cols):
                max_path = max(max_path, dfs(i, j, set()))

    return max_path

grid = [
    [9,  9, 4],
    [6,  0, 8],
    [2,  1, 1]
]
print(f"Expected: 18, Longest increasing path sum: {find_longest_increasing_path(grid)}") # 1 -> 2 -> 6 -> 9

grid = [
    [9, 9, 4],
    [3, 4, 5],
    [2, 1, 1]
]
print(f"Expected: 19, Longest increasing path sum: {find_longest_increasing_path(grid)}") # 1 -> 2 -> 3 -> 4 -> 9