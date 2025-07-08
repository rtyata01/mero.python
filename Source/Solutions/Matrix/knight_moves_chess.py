from collections import deque

def min_knight_moves(start, target, blocked):
    # All 8 knight moves
    moves = [(-2, -1), (-2, 1), (2, -1), (2, 1),
             (-1, -2), (-1, 2), (1, -2), (1, 2)]

    # Board size
    N = 8    
    visited = set()
    sx, sy = start
    tx, ty = target

    if start == target:
        return 0
    if (sx, sy) in blocked or (tx, ty) in blocked:
        return -1  # impossible if start or target is blocked

    queue = deque()
    queue.append((sx, sy, 0))  # (x, y, distance)
    visited.add((sx, sy))

    while queue:
        x, y, dist = queue.popleft()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited and (nx, ny) not in blocked:
                if (nx, ny) == (tx, ty):
                    return dist + 1
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))

    return -1  # not reachable

start = (1, 1)
target = (7, 7)
blocked = {(2, 1), (1, 2), (3, 3)}

print(f"Total Number of Knight Moves: ", min_knight_moves(start, target, blocked))

start = (0, 0)
target = (7, 7)
blocked = {(2, 1), (1, 2), (3, 3)}

print(f"Total Number of Knight Moves: ", min_knight_moves(start, target, blocked))
