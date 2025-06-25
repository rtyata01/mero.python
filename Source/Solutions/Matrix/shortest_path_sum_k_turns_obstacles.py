# In an N x M grid, you can only make at most K direction changes. 
# Find the shortest path from start to end, with moves right, down, up, left

import heapq

def min_turns_path_sum(grid, k):
    if not grid or grid[0][0] <= 0 or k <= 0:
        return -1
    
    rows, cols = len(grid), len(grid[0])
    directions = {'right': (0,1), 'down':(1,0), 'left': (0,-1), 'up': (-1, 0)}

    heap = [] 
    # start from (0,0) and travel applicable directions to add (cost, x, y, direction_index, turns)
    for dir_name, (dx, dy) in directions.items(): 
        nx, ny = 0 + dx, 0 + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            heapq.heappush(heap, (grid[0][0] + grid[nx][ny], nx, ny, dir_name, 0))

    # heap = [(3, 0, 1, 'right', 0), (5, 1, 0, 'down', 0)]            
    
    visited = {}
    while heap:
        cost, x, y, dir_name, turns = heapq.heappop(heap)

        if (x, y) == (rows - 1, cols - 1):
            return cost
        
        key = (x, y, dir_name, turns)
        if key in visited and visited[key] <= cost:
            continue
        visited[key] = cost


        for new_dir, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] > 0:
                new_turns = turns + (1  if new_dir != dir_name else 0)
                if new_turns <= k:
                    new_cost = cost + grid[nx][ny]
                    heapq.heappush(heap, (new_cost, nx, ny, new_dir, new_turns))
    
    return -1  # path not found


grid = [
    [1, 2, -4],
    [4, 1, 2],
    [1, 5, 1]
]

K = 0 # 1-2-4-2-1
result = min_turns_path_sum(grid, K)
print("Expected: 12, Minimum turns to reach:", result)

K = 1 # 1-2-4-2-1
result = min_turns_path_sum(grid, K)
print("Expected: 12, Minimum turns to reach:", result)

K = 2 # 1-4-1-2-1
result = min_turns_path_sum(grid, K)
print("Expected: 9, Minimum turns to reach:", result)

K = 3 # 1-2-1-2-1
result = min_turns_path_sum(grid, K)
print("Expected: 7, Minimum turns to reach:", result)

K = 4 # 1-2-1-2-1
result = min_turns_path_sum(grid, K)
print("Expected: 7, Minimum turns to reach:", result)
