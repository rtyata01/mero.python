# grid size m * n, 
# cell with 0 is blocker
# find max gold path from one cell to another.

def find_maximum_gold(grid):
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)] # up, down, left, right
    
    def dfs(x, y, visited) -> int:
        visited.add((x, y))
        max_gold = 0
        
        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != 0 and (nx, ny) not in visited:
                max_gold = max(max_gold, dfs(nx, ny, visited))

        visited.remove((x,y))
        return grid[x][y] + max_gold
    
    max_total_gold = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                max_total_gold = max(max_total_gold, dfs(i, j, set()))
                                                                  
    return max_total_gold
    
grid = [
    [0,6,0],
    [5,8,7],
    [0,9,0]
]
print(find_maximum_gold(grid))  # Output: One path with max gold: 9 → 8 → 7 → (total = 24)

# Time complexity = o(rows * cols * k) k is the number of cells expect 0 cell.
# For improved and complex solution, you can use bit masking and memorization soultions, on top of dfs.
