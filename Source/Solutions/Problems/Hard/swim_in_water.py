# You're given an N x N grid grid[i][j], where each cell has an elevation.
# You start at (0, 0) and want to reach (N-1, N-1).
# At time t, you can enter any square with elevation ≤ t.
# You can move up/down/left/right to adjacent cells.

import heapq

def swimInWater(grid):
    N = len(grid)
    visited = [[False]*N for _ in range(N)]
    heap = [(grid[0][0], 0, 0)]  # (elevation, row, col)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while heap:
        time, r, c = heapq.heappop(heap)
        if r == N - 1 and c == N - 1:
            return time
        if visited[r][c]:
            continue
        visited[r][c] = True
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                heapq.heappush(heap, (max(time, grid[nr][nc]), nr, nc))

grid= [
    [0,2],
    [1,3]
]
print(f"Minimum time to reach destination is: ", swimInWater(grid))

grid = [
  [0, 1, 2, 3, 4],
  [24,23,22,21,5],
  [12,13,14,15,16],
  [11,17,18,19,20],
  [10, 9, 8, 7, 6]
]
print(f"Minimum time to reach destination is: ", swimInWater(grid))

grid = [
  [0, 1, 2, 3, 4],
  [24,23,22,21,5],
  [12,13,14,15,16],
  [11,17,18,19,20],
  [30, 9, 8, 7, 6]
]
print(f"Minimum time to reach destination is: ", swimInWater(grid))

grid = [
  [0, 1, 2, 3, 4],
  [24,23,22,21,5],
  [12,13,14,35,16],
  [11,17,18,19,20],
  [30, 9, 8, 7, 6]
]
print(f"Minimum time to reach destination is: ", swimInWater(grid))