# start from any cell, but end at bottom right cell.
# find the maximum sum path reaching to end.

def maximum_path_sum(grid):
    if not grid or not grid[0][0]:
        return -1
    
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0)] # right, down
    directions += [(0, -1), (-1, 0)] # left, up
    max_total_cost = 0

    def dfs(x, y, visited):
        if (x,y) == (rows - 1, cols - 1):
            return grid[x][y]
        
        visited.add((x,y))
        max_cost = 0
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] > 0 and (nx, ny) not in visited):
                max_cost = max(max_cost, dfs(nx, ny, visited))

        visited.remove((x,y))
        return grid[x][y] + max_cost

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] > 0:
                max_total_cost = max(max_total_cost, dfs(i, j, set()))
                
    return max_total_cost

grid = [
    [-1, 2, 8],
    [4, -1, 2],
    [1, 5, 1]
]

result = maximum_path_sum(grid)
print("Expected: 13, Maximum cost to reach:", result)

grid = [
    [1, 2, 3],
    [4, -1, 2],
    [1, 5, 1]
]

result = maximum_path_sum(grid)
print("Expected: 19, Maximum cost to reach:", result)


grid = [
    [-1, 4, 1],
    [2, -1, 5],
    [8, 2, 1]
]

result = maximum_path_sum(grid)
print("Expected: 13, Maximum cost to reach:", result)

