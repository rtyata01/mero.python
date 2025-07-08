# In an N x M grid, you can only make at most K direction changes. 
# Find the shortest path from start to end.

from collections import deque
import heapq

def shortest_path_k_turns(grid, start, end, k):
    if not grid or k <= 0:
        return -1
    
    if start == end:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    sx, sy = start
    ex, ey = end    
    queue = deque()
    visited = set()
    
    for di, (dx, dy) in enumerate(directions): # di = direction index, 0 = up, 1= down, 2 = left, 3 = right 
        nx, ny = sx + dx, sy + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
            queue.append((nx, ny, di, 0, 1)) # (x, y, direction_index, turns, steps)
            visited.add((nx, ny, di, 0))
    
    while queue:
        x, y, dir_index, turns, steps = queue.popleft()

        if (x, y) == (ex, ey):
            return steps

        for di, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_turns = turns + (di != dir_index)  # True = 1, False = 0
                if new_turns <= k and (nx, ny, di, new_turns) not in visited:
                    queue.append((nx, ny, di, new_turns, steps + 1))
    
    return -1 

grid = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
print(f"Shortest path:", shortest_path_k_turns(grid, (0,0), (4,4), 3))
print(f"Shortest path:", shortest_path_k_turns(grid, (2,0), (4,4), 3))
print(f"Shortest path:", shortest_path_k_turns(grid, (0,4), (4,4), 3))
print(f"Shortest path:", shortest_path_k_turns(grid, (2,4), (4,3), 3))

grid = [
  [0, 0, 0],
  [1, 1, 1],
  [0, 0, 0]
]
print(f"Shortest path:", shortest_path_k_turns(grid, (0,0), (2,2), 1))
