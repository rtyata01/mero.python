import random

# Simulate rolling a six-sided die 10000 times
rolls = [random.randint(1, 6) for _ in range(10000)]

# Count occurrences of each face
counts = {i: rolls.count(i) for i in range(1, 7)}

# Calculate probabilities
probabilities = {face: count / 10000 for face, count in counts.items()}

print("Face counts:", counts)
print("Estimated probabilities:", probabilities)