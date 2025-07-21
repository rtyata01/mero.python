# Problem: Rotate Image or Given an n x n 2D matrix representing an image, rotate it 90 degrees clockwise in-place.
# First transpose the matrix (swap elements across the diagonal), then reverse each row.

def rotate_clockwise(matrix: list[list[int]]):
    n = len(matrix)
    
    # Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
        
    return matrix
        
# Time Complexity: O(n²)
# Space Complexity: O(1)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"Input:", matrix)
matrix_90 = rotate_clockwise(matrix)
print(f"Rotate 90:", matrix_90)
matrix_180 = rotate_clockwise(matrix_90)
print(f"Rotate 180:", matrix_180)
matrix_270 = rotate_clockwise(matrix_180)
print(f"Rotate 270:", matrix_270)
matrix_360 = rotate_clockwise(matrix_270)
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
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]


"""