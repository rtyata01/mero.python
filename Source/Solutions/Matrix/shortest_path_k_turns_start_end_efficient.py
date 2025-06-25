from collections import deque

def shortest_path_with_k_turns(grid, start, end, k):
    if not grid:
        return -1
    
    rows, cols = len(grid), len(grid[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right

    sx, sy = start
    ex, ey = end

    visited = [[[float('inf')] * 4 for _ in range(cols)] for _ in range(rows)]
    queue = deque()

    for d, (dx, dy) in enumerate(directions):
        nx, ny = sx + dx, sy + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
            visited[nx][ny][d] = 0
            queue.append((nx, ny, d, 0, 1))  # initialize x, y, direction, turns, steps

    while queue:
        x, y, dir, turns, steps = queue.popleft()
        if (x, y) == (ex, ey):
            return steps

        for new_dir, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_turns = turns + (new_dir != dir)
                if new_turns <= k and new_turns < visited[nx][ny][new_dir]:
                    visited[nx][ny][new_dir] = new_turns
                    queue.append((nx, ny, new_dir, new_turns, steps + 1))

    return -1  # not reachable within k turns

grid = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
print(f"Shortest path:", shortest_path_with_k_turns(grid, (0,0), (4,4), 3))
print(f"Shortest path:", shortest_path_with_k_turns(grid, (2,0), (4,4), 3))
print(f"Shortest path:", shortest_path_with_k_turns(grid, (0,4), (4,4), 3))
print(f"Shortest path:", shortest_path_with_k_turns(grid, (2,4), (4,3), 3))

grid = [
  [0, 0, 0],
  [1, 1, 1],
  [0, 0, 0]
]
print(f"Shortest path:", shortest_path_with_k_turns(grid, (0,0), (2,2), 1))
