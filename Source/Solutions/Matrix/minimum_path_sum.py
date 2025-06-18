import heapq

def minimum_path_sum(grid):
    if not grid or grid[0][0] <= 0:
        return -1
    
    rows, cols = len(grid), len(grid[0])
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    heap = [(grid[0][0], 0, 0)]
    visited = set()
    
    while heap:
        cost, x, y = heapq.heappop(heap)
        
        if (x, y) in visited:
            continue
        
        visited.add((x,y))
        
        if x == rows - 1 and y == cols - 1:
            return cost
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] > 0:
                new_cost = cost + grid[nx][ny]
                heapq.heappush(heap, (new_cost, nx, ny))
                
    return -1

grid = [
    [1, 2, 4],
    [4, 1, 2],
    [1, 5, 1]
]

# 1-2-1-2-1
result = minimum_path_sum(grid)
print("Expected: 7, Minimum turns to reach:", result)

grid = [
    [1, 3, 1, 2],
    [1, -10, -9, 3],
    [2, 1, -8, 1],
    [4, 2, 1, 1]
]
print("Expected: 9, Minimum weight path (4 directions):", minimum_path_sum(grid))

