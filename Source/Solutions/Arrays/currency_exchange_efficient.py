# use dynamic programming for finding minimum numbe rof coins, regardless of order or value.

def get_min_change(denominations, amount):
    dp = [float('inf')] * (amount + 1) # holds the minimum number of coins, fill with infinity
    prev = [-1] * (amount + 1) # coin used to reach amount, fill with -1
    dp[0] = 0  # 0 coins needed to make amount 0

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
denominations = [9, 6, 1]
amount = 12 # Amount in cents

result = get_min_change(denominations, amount)
print(f"Change for {amount} cents:", result)

# dp[9-9] + 1 < inf = 0 + 1 < inf = dp[9] = 1, prev[9] = 9
# dp[6-6] + 1 < inf = 0 + 1 < inf = dp[6] = 1, prev[6] = 6
# dp[12-6] + 1 < inf = 1 + 1 < inf = dp[12] = 2, prev[12] = 6
# #
# coin = prev[12] = 6
# result = { 6 : 1 }
# coin = prev[6] = 6
# result = { 6 : 2 }

denominations = [1, 9, 6]
amount = 12 # Amount in cents

result = get_min_change(denominations, amount)
print(f"Change for {amount} cents:", result)