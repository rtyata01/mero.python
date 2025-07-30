# use dynamic programming for finding minimum numbe rof coins, regardless of order or value.

# steps:
# initialize dp[i] = minimum number of coinds needed to make amount i, dp[0] = 0, zero coins to make zero.
# prev[i] = last coin used ot make amount i optimally.

def get_min_change(denominations, amount):
    dp = [float('inf')] * (amount + 1) # Start with "infinite" coins needed
    dp[0] = 0   # 0 coins needed to make amount 0
    prev = [-1] * (amount + 1)  # No coin used initially

    for coin in denominations:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                prev[i] = coin

    if dp[amount] == float('inf'):
        return None  # No solution possible

    # Reconstruct coin combination
    result = {}
    while amount > 0:
        coin = prev[amount]
        if coin == -1:
            return None
        
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result

# Example
denominations = [1, 4, 3]
amount = 6 # Amount in cents
result = get_min_change(denominations, amount)
print(f"Change for {amount} cents:", result)

# coin 1, i=1 to 6, dp = [0, 1, 2, 3, 4, 5, 6] prev = [-1, 1, 1, 1, 1, 1, 1]
# coin 4, i=4 to 6, dp = [0, 1, 2, 3, 1, 2, 3] prev = [-1, 1, 1, 1, 4, 4, 4]
# coin 3, i=3 to 6, dp = [0, 1, 2, 1, 1, 2, 2] prev = [-1, 1, 1, 3, 4, 4, 3]

# Example
denominations = [9, 6, 1]
amount = 12 # Amount in cents

result = get_min_change(denominations, amount)
print(f"Change for {amount} cents:", result)

# dp = [0, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞]
# prev = [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
# coin 9, dp[9-9] + 1 < inf = 0 + 1 < inf = dp[9] = 1, prev[9] = 9
# coin 6, dp[6-6] + 1 < inf = 0 + 1 < inf = dp[6] = 1, prev[6] = 6
# coin 6, dp[12-6] + 1 < inf = 1 + 1 < inf = dp[12] = 2, prev[12] = 6
# #
# coin = prev[12] = 6
# result = { 6 : 1 }
# coin = prev[6] = 6
# result = { 6 : 2 }

denominations = [1, 9, 6]
amount = 12 # Amount in cents

result = get_min_change(denominations, amount)
print(f"Change for {amount} cents:", result)