# Given a grid where each cell has a height, 
# find a path from top-left to bottom-right such that the maximum difference between adjacent heights in the path is minimized.

import heapq

def minimumEffortPath(heights):
    m, n = len(heights), len(heights[0])
    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    INF = float('inf')
    effort = [[INF] * n for _ in range(m)] # Set Grid with Infinity.
    effort[0][0] = 0
    heap = [(0, 0, 0)]  # (effort, row, col)

    while heap:
        curr_effort, x, y = heapq.heappop(heap)
        if x == m - 1 and y == n - 1:
            return curr_effort
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                next_effort = max(curr_effort, abs(heights[x][y] - heights[nx][ny]))
                if effort[nx][ny] > next_effort:
                    effort[nx][ny] = next_effort
                    heapq.heappush(heap, (next_effort, nx, ny))


heights = [
    [1, 2, 2],
    [3, 8, 2],
    [5, 3, 5]
]

print(f"Expected height:2, Minumum Height: ", minimumEffortPath(heights))

"""
(0,0) height=1
-> (0,1) height=2  | diff = 1
-> (0,2) height=2  | diff = 0
-> (1,2) height=2  | diff = 0
-> (2,2) height=5  | diff = 3 (But this step has effort 3, so we tried another route)

Better path is:

(0,0) height=1
-> (1,0) height=3  | diff = 2
-> (2,0) height=5  | diff = 2
-> (2,1) height=3  | diff = 2
-> (2,2) height=5  | diff = 2
"""
