# Hard: You're given a binary n x n grid where:
# 1 represents land
# 0 represents water
# An island is a group of connected 1s (connected 4-directionally: up, down, left, right).
# Find how many islands and the size of largest island

def count_island_size(grid):
    if not grid:
        return 0
    
    n = len(grid)
    island_id = 2
    island_area = {}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(x, y, id):
        area = 1
        grid[x][y] = id
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                area += dfs(nx, ny, id)
        return area


    # Step 1: Label all islands and calculate areas
    for x in range(n):
        for y in range(n):
            if grid[x][y] == 1:
                area = dfs(x, y, island_id)
                island_area[island_id] = area
                island_id += 1

    return island_area

# Time complexity= o(m * n)
# Space complexity= o(m * n)

# Before DFS
grid = [
  [1, 0],
  [0, 1]
]

# After DFS labeling:
#[2, 0]    # island_id=2, size=1
#[0, 3]    # island_id=3, size=1
island_to_size = count_island_size(grid)
print(f"island count: {len(island_to_size)}, island with max area: {max(island_to_size.values())}" )

grid = [
    [1, 0, 1, 1],
    [1, 0, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 0, 0]
]

# After DFS labeling:
#[2, 0, 3, 3]  # island_id=2, size=2
#[2, 0, 3, 0]  # island_id=3, size=6
#[0, 3, 3, 3]  # island_id=4, size=1
#[4, 0, 0, 0]  
island_to_size = count_island_size(grid)
print(f"island count: {len(island_to_size)}, island with max area: {max(island_to_size.values())}" )

# Before DFS
grid = [
    [1, 0, 1, 1],
    [1, 0, 1, 0],
    [0, 1, 1, 1],
    [1, 1, 0, 0]
]
# After DFS labeling:
[2, 0, 3, 3]  # island_id=2, size=2
[2, 0, 3, 0]  # island_id=3, size=8
[0, 3, 3, 3]
[3, 3, 0, 0]
island_to_size = count_island_size(grid)
print(f"island count: {len(island_to_size)}, island with max area: {max(island_to_size.values())}" )