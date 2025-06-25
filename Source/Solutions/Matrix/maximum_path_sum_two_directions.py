def maximum_path_sum(grid):
    if not grid or grid[0][0] <= 0:
        return -1
    
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0)] # right, down

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

    result = dfs(0, 0, set())            
    return result

grid = [
    [-1, 2, 8],
    [4, -1, 2],
    [1, 5, 1]
]

result = maximum_path_sum(grid)
print("Expected: -1, Maximum cost to reach:", result)

grid = [
    [1, 2, 3],
    [4, -1, 2],
    [1, 5, 1]
]

result = maximum_path_sum(grid)
print("Expected: 12, Maximum cost to reach:", result)

