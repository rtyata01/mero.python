import numpy as np

# Define matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[2, 0],
              [1, 3]])

# Matrix addition
add_matrix = A + B

# Matrix subtraction
sub_matrix = A - B

# Matrix multiplication
mult_matrix = np.dot(A, B)

# Determinant of A
det_A = np.linalg.det(A)

# Inverse of A
inv_A = np.linalg.inv(A)

print(f"A + B =\n{add_matrix}\n")
print(f"A - B =\n{sub_matrix}\n")
print(f"A * B =\n{mult_matrix}\n")
print(f"det(A) = {det_A:.2f}\n")
print(f"A^-1 =\n{inv_A}")