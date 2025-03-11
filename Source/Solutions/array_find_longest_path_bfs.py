from collections import deque

def find_longest_path(matrix):
    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])    
    directions = [(-1 , 0), (1 , 0), (0, -1), (0, 1)] # up, down, left, right
    max_path_length = 0
    cache = {}
    
    def bfs_traversal(i, j):
        queue = deque([(i, j)])
        cache[(i, j)] = 1 # Start with length 1 for current cell.
        max_length = 1  
        
        while queue:
            x, y = queue.popleft()
            length = cache[(x, y)]
        
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (0 <= nx < rows and 0 <= ny < cols) and matrix[nx][ny] == 1 and (nx, ny) not in cache:
                    cache[(nx, ny)] = length + 1
                    max_length = max(max_length, length + 1)
                    queue.append((nx, ny))
        
        return max_length
            
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and (i, j) not in cache:
                max_path_length = max(max_path_length, bfs_traversal(i, j,))
    
    return max_path_length

# time complexity = o(directions * rows * cols)
# BFS uses queue and it does not use backtracking. This is suitable for both smaller and larger matrix. The bigger the matrix, it will consume more memory space.
matrix = [
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1],
    [1, 0, 1, 0]
]
print(f"Expected: 6, Longest Path: {find_longest_path(matrix)}") 

matrix = [[0, 1, 1]]
print(f"Expected: 2, Longest Path: {find_longest_path(matrix)}") 

matrix = [
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]
]  
print(f"Expected: 0, Longest Path: {find_longest_path(matrix)}") 
