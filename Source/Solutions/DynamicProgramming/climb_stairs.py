# If you can climb either 1 step or 2 steps, then find the distinct ways you can climb the staircase of n steps.

def climb_stairs(n):
    if n == 0 or n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Example usage:
print(f"Expected: 8: Computed Ouptut: ", climb_stairs(5))  # Output: 8
# ways(i) = ways(i-1) + ways(i-2)

# dp[2]  = dp[1] + dp[0]    = 1 + 1 = 2     # [1,1], [2]
# dp[3]  = dp2[2] + dp[1]   = 2 + 1 = 3     # [1,1,1], [1,2] # [2,1]
# dp[4]  = dp[3] + [dp2]    = 3 + 2 = 5     # [1,1,1,1], [1,1,2] [1,2,1], # [2,1,1], [2,2]
# dp[5]  = dp[4] + dp[3]    = 5 + 3 = 8     # [1,1,1,1,1], [1,1,1,2] [1,1,2,1], [1,2,1,1] [1,2,2] # [2,1,1,1], [2,1,2] [2,2,1]

def climb_stairs_with_paths(n):
    if n == 0:
        return [[]]  # One way: take no steps

    # dp[i] will store all the paths to reach step i
    dp = [[] for _ in range(n + 1)]
    dp[0] = [[]]  # One way to be at ground level

    for i in range(1, n + 1):
        if i - 1 >= 0:
            for path in dp[i - 1]:
                dp[i].append(path + [1])
        if i - 2 >= 0:
            for path in dp[i - 2]:
                dp[i].append(path + [2])

    return dp[n]

# Example usage:
n = 5
paths = climb_stairs_with_paths(n)
print(f"Total ways to climb {n} steps: {len(paths)}")
for i, path in enumerate(paths, 1):
    print(f"Way {i}: {path}")

# Time Complexity = O(n⋅2^n)

# 2^n : Number of unique paths (from the Fibonacci growth)
# n: Time to copy and append to a path of length up to n