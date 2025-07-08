# In an N x M grid, you can only make at most K direction changes. 
# Find the shortest path from start to end.

from collections import deque

def min_turns_path(grid, k):
    if not grid or k <= 0:
        return -1
    
    rows, cols = len(grid), len(grid[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    queue = deque()

    # 0 = up, 1= down, 2 = left, 3 = right 
    for i, (dx, dy) in enumerate(directions):
        queue.append((0, 0, i, 0))  # (x, y, direction_index, turns)
    
    visited = set()
    while queue:
        x, y, dir_idx, turns = queue.popleft()

        if (x, y, dir_idx, turns) in visited:
            continue
        visited.add((x, y, dir_idx, turns))

        if (x, y) == (rows - 1, cols - 1):
            return turns

        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            new_turns = turns + (i != dir_idx)
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and new_turns <= k:
                queue.append((nx, ny, i, new_turns))
    
    return -1  # path not found


grid = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]
k = 3

result = min_turns_path(grid, k)
print("Expected: 3, Minimum turns to reach: ", result)


