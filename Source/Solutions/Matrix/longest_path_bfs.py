from collections import deque

def find_longest_path(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1 , 0), (1 , 0), (0, -1), (0, 1)] # up, down, left, right
    # directions  += [(-1, -1), (-1, 1), (1, -1), (1, 1)] # diagonal traversal
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y, {(x, y)}, 1))  # (current x, y, visited set, path length)
        max_len = 1

        while queue:
            cx, cy, visited, length = queue.popleft()
            max_len = max(max_len, length)

            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if (0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] == 1 and (nx, ny) not in visited):
                    queue.append((nx, ny, visited | {(nx, ny)}, length + 1)) # union visited.union({(nx, ny)})

        return max_len

    max_path = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                max_path = max(max_path, bfs(i, j))

    return max_path

# time complexity = o(directions * rows * cols)
# BFS uses queue and it does not use backtracking. This is suitable for both smaller and larger matrix. 
# The bigger the matrix, it will consume more memory space.
# Choose BFS for shortest path problems.

matrix = [
    [1, 0, 1, 1],
    [1, 0, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 0, 0]
]
print(f"Expected: 5, Longest Path: {find_longest_path(matrix)}") 

matrix = [[0, 1, 1]]
print(f"Expected: 2, Longest Path: {find_longest_path(matrix)}") 

matrix = [
    [0], 
    [1], 
    [1]
]  
print(f"Expected: 0, Longest Path: {find_longest_path(matrix)}") 

matrix = [
    [1, 0, 1, 1],
    [1, 0, 1, 0],
    [0, 1, 1, 1],
    [1, 1, 0, 0]
]
print(f"Expected: 7, Longest Path: {find_longest_path(matrix)}")