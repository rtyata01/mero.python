# Problem: Given an n x n 2D matrix representing an image, rotate it 90 degrees anti clockwise in-place.
# First transpose the matrix (swap elements across the diagonal), then reverse each column.

def rotate_anti_clockwise(matrix: list[list[int]]):
    n = len(matrix)
    
    # Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
     # Step 2: Reverse each column
    for j in range(n):
        for i in range(n // 2):
            matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]
        
    return matrix
        
# Time Complexity: O(n²)
# Space Complexity: O(1)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"Input:", matrix)
matrix_90 = rotate_anti_clockwise(matrix)
print(f"Rotate 90:", matrix_90)
matrix_180 = rotate_anti_clockwise(matrix_90)
print(f"Rotate 180:", matrix_180)
matrix_270 = rotate_anti_clockwise(matrix_180)
print(f"Rotate 270:", matrix_270)
matrix_360 = rotate_anti_clockwise(matrix_270)
print(f"Rotate 360:", matrix_360)

""" 
After transposing, 
[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

After row reverse
[
    [3, 6, 9],
    [2, 5, 8],
    [1, 4, 7]
]


"""