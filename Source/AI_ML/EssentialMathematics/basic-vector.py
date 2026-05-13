import numpy as np

# Define vectors
a = np.array([2, 3, 4])
b = np.array([1, 0, -1])

# Vector addition
add = a + b

# Vector subtraction
sub = a - b

# Dot product
# a⋅b = a1b1 + a2b2 + a3b3
dot = np.dot(a, b)

# Cross product
# a×b = ​[a2​b3 ​−a3​b2​, a3​b1​−a1​b3​, a1​b2​−a2​b1]​​​
cross = np.cross(a, b)

# Magnitude of a
magnitude_a = np.linalg.norm(a)

print(f"a + b = {add}")
print(f"a - b = {sub}")
print(f"a · b = {dot}")
print(f"a × b = {cross}")
print(f"|a| = {magnitude_a:.2f}")