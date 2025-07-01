from collections import deque

def find_optimal_well_location(grid):
    if not grid or not grid[0]:
        return None, None

    rows, cols = len(grid), len(grid[0])
    total_distance = [[0] * cols for _ in range(rows)]
    reachable_count = [[0] * cols for _ in range(rows)]

    houses = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 'H']  # houses = [(0, 0), (2, 0), (2, 3)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for hr, hc in houses:
        visited = [[False] * cols for _ in range(rows)]
        queue = deque([(hr, hc, 0)])
        visited[hr][hc] = True

        while queue:
            r, c, dist = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == '.'):
                    visited[nr][nc] = True
                    total_distance[nr][nc] += dist + 1
                    reachable_count[nr][nc] += 1
                    queue.append((nr, nc, dist + 1))

    min_dist = float('inf')
    best_cell = None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.' and reachable_count[r][c] == len(houses):
                if total_distance[r][c] < min_dist:
                    min_dist = total_distance[r][c]
                    best_cell = (r, c)

    return best_cell, (min_dist if best_cell else None)

grid = [
    ['H', '.', '.', 'T'],
    ['.', 'T', '.', '.'],
    ['H', '.', '.', 'H']
]

location, total_distance = find_optimal_well_location(grid)
print("Best well location:", location)
print("Minimum total distance:", total_distance)

"""
# After BFS traversal from all houses, total distance and reachable counts will be below.

total_distance = [
 [0, 5, 5, 0],
 [2, 0, 8, 9],
 [0, 9, 7, 0]
]

reachable_count = [
 [0, 2, 2, 0],
 [2, 0, 3, 3],
 [0, 3, 3, 0]
]

# The best well location is  (2,2), where weight = 7 and reachable count is 3.
"""