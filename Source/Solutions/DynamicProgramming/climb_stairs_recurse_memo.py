def climb_stairs(stairs, memo=None):
    if memo is None:
        memo = {}
        
    if stairs == 1:
        return 1
    if stairs == 2:
        return 2
    
    if stairs in memo:
        return memo[stairs]
    
    memo[stairs] = climb_stairs(stairs-1) + climb_stairs(stairs-2)
    return memo[stairs]

# Time complexity	O(n)
# Space complexity	O(n)

result = climb_stairs(5)
print(f"Number of ways to climb stairs: {result}")

def ways_to_climb_stairs(stairs, memo=None):
    if memo is None:
        memo = {}

    if stairs == 0:
        return [[]]  # One valid path: no steps (already at top)
    if stairs < 0:
        return []    # No valid paths if steps negative

    if stairs in memo:
        return memo[stairs]

    paths = []
    for step in [1, 2]:
        for sub_path in ways_to_climb_stairs(stairs - step, memo):
            paths.append([step] + sub_path)

    memo[stairs] = paths
    return paths

# Time Complexity:	O(2^n) — exponential in n because all paths are generated
# Space Complexity:	O(2^n * n) — exponential space to store all paths (each up to length n)

# Example usage:
stairs = 5
paths = ways_to_climb_stairs(stairs)
print(f"Total ways to climb {stairs} steps: {len(paths)}")
for i, path in enumerate(paths, 1):
    print(f"Way {i}: {path}")