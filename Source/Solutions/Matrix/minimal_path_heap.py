import heapq

def min_path_weight_all_directions(grid):
    if not grid or grid[0][0] == -1:
        return -1

    rows, cols = len(grid), len(grid[0])
    INF = float('inf')
    dist = [[INF] * cols for _ in range(rows)]
    dist[0][0] = grid[0][0]

    # Min-heap: (current_cost, row, col)
    heap = [(grid[0][0], 0, 0)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    while heap:
        cost, x, y = heapq.heappop(heap)

        if (x, y) == (rows - 1, cols - 1):
            return cost  # Reached destination

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != -1:
                new_cost = cost + grid[nx][ny]
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heapq.heappush(heap, (new_cost, nx, ny))

    return -1  # Destination not reachable


grid = [
    [1, 3, 1, 2],
    [1, -1, -1, 3],
    [2, 1, -1, 1],
    [4, 2, 1, 1]
]
print("Expected: 9, Minimum weight path (4 directions):", min_path_weight_all_directions(grid))


grid = [
    [1, 3, 1, 2],
    [1, 1, -1, 3],
    [2, 1, 1, -1],
    [4, 2, 1, 1]
]
print("Expected: 7, Minimum weight path (4 directions):", min_path_weight_all_directions(grid))
