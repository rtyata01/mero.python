#You're given a notepad that initially displays a single character 'A'. You have two actions available to perform on this notepad for each step:
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

class Solution:
    def min_operations(self, n: int) -> int:
        cache = {}
        
        def count_steps(k):
            if k == 1:
                return 0
            if k in cache:
                return cache[k]
            
            for i in range(2, k + 1):
                if k % i == 0:
                    cache[k] = count_steps(k // i) + i
                    return cache[k]
        
        return count_steps(n)


sol = Solution()
n = 4
print(f"Print A [{n}] times, Number of operations: {sol.min_operations(n)}")  

n = 7
print(f"Print A [{n}] times, Number of operations: {sol.min_operations(n)}")       

n = 9
print(f"Print A [{n}] times, Number of operations: {sol.min_operations(n)}")            