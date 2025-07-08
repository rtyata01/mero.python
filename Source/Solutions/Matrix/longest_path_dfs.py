def find_longest_path(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1 , 0), (1 , 0), (0, -1), (0, 1)] # up, down, left, right
    # directions  += [(-1, -1), (-1, 1), (1, -1), (1, 1)] # diagonal traversal
    
    # visited trackes the DFS path and it prevents from revisiting nodes(and forming cycles).
    # memo is used to cache the earlier paths and it does not consisder the visisted states.
    # therefore, do not use memo and visisted together.
    # use only memo, no visisted, if matrix is DAG (Directly Acyclic Graph) i.e. no cycles.
    
    def dfs(x, y, visited):
        visited.add((x, y))
        max_len = 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] == 1 and (nx, ny) not in visited):
                max_len = max(max_len, 1 + dfs(nx, ny, visited))

        visited.remove((x, y))  # Backtrack
        return max_len

    max_path = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                max_path = max(max_path, dfs(i, j, set()))

    return max_path

# time complexity = o(directions * rows * cols)
# DFS uses stack, i.e. recursive backtracking. This is normally suitable if the matrix size is fixed and smaller like 8 * 8. 
# Recursive logic will be complex and hard to manage, when the matrix size grows.
# Choose DFS for exhaustive search or problems involving backtracking.

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
