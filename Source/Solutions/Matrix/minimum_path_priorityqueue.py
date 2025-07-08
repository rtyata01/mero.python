# You are given an N x M grid where each cell has a cost. 
# Some cells are blocked (cannot be visited). 
# Find the minimum cost to reach the bottom-right from the top-left.
# PriorityQueue = min heap.

import heapq

def min_cost_path(grid):
    if not grid or grid[0][0] <= 0:
        return -1
    
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1), (1,0), (-1,0), (0,-1)] 
    heap = [(grid[0][0], 0, 0)]  # (cost, x, y)
    visited = set()

    while heap:
        cost, x, y = heapq.heappop(heap)
        if (x, y) in visited:
            continue
        if (x, y) == (rows - 1, cols - 1):
            return cost
        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] > 0):  # -1 is an obstacle
                new_cost = cost + grid[nx][ny]
                heapq.heappush(heap, (new_cost, nx, ny))
    return -1  # path not found

grid = [
    [1, 3, 1, 2],
    [1, -1, -1, 3],
    [2, 1, -1, 1],
    [4, 2, 1, 1]
]
print("Expected: 9, Minimum weight path (4 directions):", min_cost_path(grid))

grid = [
    [1, 3, 1, 2],
    [1, 1, -1, 3],
    [2, 1, 1, -1],
    [4, 2, 1, 1]
]
print("Expected: 7, Minimum weight path (4 directions):", min_cost_path(grid))

grid = [
    [1,  1,  100],
    [1, -1,  1],
    [1,  1,   1]
]
print("Expected: 5, Minimum weight path (4 directions):", min_cost_path(grid))