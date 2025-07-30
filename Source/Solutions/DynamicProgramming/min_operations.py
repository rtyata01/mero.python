# You're given a notepad that initially displays a single character 'A'. 
# You have two actions (i.e. 2 Keys Keyboard problem):
# Copy All: It allows you to copy everything on the screen.
# Paste: You can paste the characters which are copied last time.
# Given an integer n, return the minimum number of operations to print the character 'A' exactly n times on the screen.

"""
You need 4 operations to get 4 'A's:
Copy All (A)
Paste → AA
Copy All (AA)
Paste → AAAA
"""

def min_operations_to_print_A(target_count: int) -> int:
    if target_count < 1:
        raise ValueError("target_count must be a positive integer greater than or equal to 1")
    
    total_operations = 0
    current_factor = 2   # refers 2 operations

    while target_count > 1:
        while target_count % current_factor == 0:
            target_count //= current_factor     # Reduce the problem
            total_operations += current_factor  # Copy + Paste steps
        current_factor += 1  # Move to next possible factor

    return total_operations

# Time Complexity: 
    # O(√n), where n is target_count and n i prime number.
    # O(log n), where n is power of 2
# Space Complexity: O(1) constand space

for i in range(1, 12):
    print(f"Print A [{i}] times, Number of operations: {min_operations_to_print_A(i)}") 
