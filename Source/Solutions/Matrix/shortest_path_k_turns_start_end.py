# In an N x M grid, you can only make at most K direction changes. 
# Find the shortest path from start to end.

from collections import deque
import heapq

def shortest_path_k_turns(grid, start, end, k):
    if start == end:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    sx, sy = start
    ex, ey = end    
    queue = deque()
    visited = set()
    
    for i, (dx, dy) in enumerate(directions): # 0 = up, 1= down, 2 = left, 3 = right 
        nx, ny = sx + dx, sy + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
            queue.append((1, nx, ny, i, 0)) # (steps, x, y, direction_index, turns)
            visited.add((nx, ny, i, 0))
    
    while queue:
        steps, x, y, dir_idx, turns = queue.popleft()

        if (x, y) == (ex, ey):
            return steps

        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_turns = turns + (i != dir_idx)
                if new_turns <= k and (nx, ny, i, new_turns) not in visited:
                    queue.append((steps + 1, nx, ny, i, new_turns))
    
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
