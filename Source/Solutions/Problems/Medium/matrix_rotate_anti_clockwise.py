# Problem: Given an n x n 2D matrix representing an image, rotate it 90 degrees anti clockwise in-place.
# First transpose the matrix (swap elements across the diagonal), then reverse each column.

# In-place rotation, only works for square n * n, and it does not work for n * m
def rotate_anti_clockwise(matrix: list[list[int]]):
    n = len(matrix)
    
    # Transpose (i, j) ->  (j, i)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # Step 2: Reverse each column
    for j in range(n):
        for i in range(n // 2):
            matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]
        
    return matrix
        
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Last column, becomes first row
# previous coulmn, becomes second row
def rotate_anti_clockwise_brute_force(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    m = len(matrix[0])
    # Rotated matrix will have dimensions m x n, instead of n * m
    result = [[0] * n for _ in range(m)]  

    # Fill in the result matrix based on rotation logic
    for i in range(n):
        for j in range(m):
            result[m - 1 - j][i] = matrix[i][j]

    return result

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]] ← Transposed
# [[3, 6, 9], [2, 5, 8], [1, 4, 7]] ← Rotated Column

print(f"Input:", matrix)
matrix_90 = rotate_anti_clockwise(matrix)
print(f"Rotate 90:", matrix_90)
matrix_180 = rotate_anti_clockwise(matrix_90)
print(f"Rotate 180:", matrix_180)
matrix_270 = rotate_anti_clockwise(matrix_180)
print(f"Rotate 270:", matrix_270)
matrix_360 = rotate_anti_clockwise(matrix_270)
print(f"Rotate 360:", matrix_360)


matrix = [
    [1, 2, 3],
    [4, 5, 6]
]


print(f"Input:", matrix)
matrix_90 = rotate_anti_clockwise_brute_force(matrix)
print(f"Rotate 90:", matrix_90)
matrix_180 = rotate_anti_clockwise_brute_force(matrix_90)
print(f"Rotate 180:", matrix_180)
matrix_270 = rotate_anti_clockwise_brute_force(matrix_180)
print(f"Rotate 270:", matrix_270)
matrix_360 = rotate_anti_clockwise_brute_force(matrix_270)
print(f"Rotate 360:", matrix_360)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Input:", matrix)
matrix_90 = rotate_anti_clockwise_brute_force(matrix)
print(f"Rotate 90:", matrix_90)
matrix_180 = rotate_anti_clockwise_brute_force(matrix_90)
print(f"Rotate 180:", matrix_180)
matrix_270 = rotate_anti_clockwise_brute_force(matrix_180)
print(f"Rotate 270:", matrix_270)
matrix_360 = rotate_anti_clockwise_brute_force(matrix_270)
print(f"Rotate 360:", matrix_360)

