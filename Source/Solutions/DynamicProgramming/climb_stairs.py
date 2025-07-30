# If you can climb either 1 step or 2 steps, then find the distinct ways you can climb the staircase of n steps.

def climb_stairs(n):
    if n == 0:
        return 1  # 1 way to stay at the bottom (do nothing)
    elif n < 0:
        return 0  # no way if steps become negative

    # ways[i] will hold the number of ways to climb i stairs
    ways = [0] * (n + 1)
    ways[0] = 1
    for i in range(1, n + 1):
        ways[i] += ways[i - 1] if i - 1 >= 0 else 0
        ways[i] += ways[i - 2] if i - 2 >= 0 else 0
        
    return ways[n]

# Time Complexity: O(n)
# Space Complexity: O(n)

# Example usage:
print(f"Expected: 8: Computed Ouptut: ", climb_stairs(5))  # Output: 8
# ways(i) = ways(i-1) + ways(i-2)

# dp[2]  = dp[1] + dp[0]    = 1 + 1 = 2     # [1,1], [2]
# dp[3]  = dp2[2] + dp[1]   = 2 + 1 = 3     # [1,1,1], [1,2] # [2,1]
# dp[4]  = dp[3] + [dp2]    = 3 + 2 = 5     # [1,1,1,1], [1,1,2] [1,2,1], # [2,1,1], [2,2]
# dp[5]  = dp[4] + dp[3]    = 5 + 3 = 8     # [1,1,1,1,1], [1,1,1,2] [1,1,2,1], [1,2,1,1] [1,2,2] # [2,1,1,1], [2,1,2] [2,2,1]
