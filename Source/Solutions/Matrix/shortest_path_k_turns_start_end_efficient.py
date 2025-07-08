from collections import deque, defaultdict

def shortest_path_with_k_turns(grid, start, end, k):
    if not grid or k <= 0:
        return -1
    
    if start == end:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right

    sx, sy = start
    ex, ey = end

    visited = {}
    queue = deque()

    for di, (dx, dy) in enumerate(directions):
        nx, ny = sx + dx, sy + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
            visited[(nx, ny, di)] = 0 # initialize (x, y, direction) = turns,
            queue.append((nx, ny, di, 0, 1))  # initialize x, y, direction, turns, steps

    while queue:
        x, y, di, turns, steps = queue.popleft()
        if (x, y) == (ex, ey):
            return steps

        for new_di, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_turns = turns + (new_di != di)
                if new_turns <= k and new_turns < visited.get((nx, ny, new_di), float('inf')):
                    visited[(nx, ny, new_di)] = new_turns
                    queue.append((nx, ny, new_di, new_turns, steps + 1))

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
