from collections import defaultdict

def find_longest_increasing_path(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    directions = [(-1 , 0), (1 , 0), (0, -1), (0, 1)] # up, down, left, right
    # directions  += [(-1, -1), (-1, 1), (1, -1), (1, 1)] # diagonal traversal
    
    # visisted = set() check is not required here, as it is used for detecting cycle during traversal.
    # For strictly increasing paths, it can't have cycles.
    # Therefore better option here is to use memorization cache.
    memo = {}
    
    def dfs(x, y):
        if (x, y) in memo:
            return memo[(x,y)]
        
        max_sum = grid[x][y]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] > grid[x][y]:
                max_sum = max(max_sum, grid[x][y] + dfs(nx, ny))

        memo[(x, y)] = max_sum
        return max_sum

    max_path = 0
    for i in range(rows):
        for j in range(cols):
                max_path = max(max_path, dfs(i, j))

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