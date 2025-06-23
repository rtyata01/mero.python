def largest_connected_island(grid):
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

    # if no island or all values are 0, then return 0.
    max_area = max(island_area.values(), default=0)

    # Step 2: Try flipping each 0
    for x in range(n):
        for y in range(n):
            if grid[x][y] == 0:
                seen = set()
                area = 1  # for the flipped 0
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        id = grid[nx][ny]
                        if id > 1 and id not in seen:
                            area += island_area[id]
                            seen.add(id)
                max_area = max(max_area, area)

    return max_area


# Time complexity= o(n^2)
# Space complexity= o(n^2)

# Before DFS
grid = [
  [1, 0],
  [0, 1]
]

# After DFS labeling:
#[2, 0]    # island_id=2, size=1
#[0, 3]    # island_id=3, size=1
print(f"Expected: 3, Largest connected island: ", largest_connected_island(grid))

# Before DFS
grid = [
  [0, 0],
  [0, 0]
]

# After DFS labeling:
#[0, 0]    
#[0, 0]    
print(f"Expected: 1, Largest connected island: ", largest_connected_island(grid))

# Before DFS
matrix = [
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
print(f"Expected: 10, Longest Path: {largest_connected_island(matrix)}") 

# Before DFS
matrix = [
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
print(f"Expected: 11, Longest Path: {largest_connected_island(matrix)}")