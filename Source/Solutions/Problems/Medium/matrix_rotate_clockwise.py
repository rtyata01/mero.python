# Problem: Rotate Image or Given an n x n 2D matrix representing an image, rotate it 90 degrees clockwise in-place.
# First transpose the matrix (swap elements across the diagonal), then reverse each row.

# In-place rotation, only works for square n * n, and it does not work for n * m
def rotate_clockwise(matrix: list[list[int]]):
    n = len(matrix)
    
    # Transpose (i,j) to (j, i)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
        
    return matrix
        
# Time Complexity: O(n²)
# Space Complexity: O(1)
# first row, becomes last column
# second row, becomes second last column
def rotate_clockwise_brute_force(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    m = len(matrix[0])
    # Rotated matrix will have dimensions m x n
    result = [[0] * n for _ in range(m)]  
    for i in range(n):
        for j in range(m):
            result[j][n - 1 - i] = matrix[i][j]
    return result

# Time Complexity: O(n²)
# Space Complexity: O(n²)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]] ← Transposed
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]] ← Rotated Rows

print(f"Input:", matrix)
matrix_90 = rotate_clockwise(matrix)
print(f"Rotate 90:", matrix_90)
matrix_180 = rotate_clockwise(matrix_90)
print(f"Rotate 180:", matrix_180)
matrix_270 = rotate_clockwise(matrix_180)
print(f"Rotate 270:", matrix_270)
matrix_360 = rotate_clockwise(matrix_270)
print(f"Rotate 360:", matrix_360)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# [4, 1]
# [5, 2]
# [6, 3]

print(f"Input:", matrix)
matrix_90 = rotate_clockwise_brute_force(matrix)
print(f"Rotate 90:", matrix_90)
matrix_180 = rotate_clockwise_brute_force(matrix_90)
print(f"Rotate 180:", matrix_180)
matrix_270 = rotate_clockwise_brute_force(matrix_180)
print(f"Rotate 270:", matrix_270)
matrix_360 = rotate_clockwise_brute_force(matrix_270)
print(f"Rotate 360:", matrix_360)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"Input:", matrix)
matrix_90 = rotate_clockwise_brute_force(matrix)
print(f"Rotate 90:", matrix_90)
matrix_180 = rotate_clockwise_brute_force(matrix_90)
print(f"Rotate 180:", matrix_180)
matrix_270 = rotate_clockwise_brute_force(matrix_180)
print(f"Rotate 270:", matrix_270)
matrix_360 = rotate_clockwise_brute_force(matrix_270)
print(f"Rotate 360:", matrix_360)
