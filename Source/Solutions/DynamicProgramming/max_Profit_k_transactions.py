# Given an array prices[] where prices[i] is the price of a stock on day i.
# An integer k representing the maximum number of transactions (buy and sell pairs).
# Find the Maximize total profit with at most k transactions.

def maxProfit(k, prices):
    if not prices or k == 0:
        return 0
    
    n = len(prices)
    
    # If k >= n/2, it's equivalent to unlimited transactions
    # we can buy and sell on every price increase, so this becomes the "unlimited transactions" case. 
    # We just sum all profits for every uptrend.
    if k >= n // 2:
        return sum(max(prices[i+1] - prices[i], 0) for i in range(n - 1))
    
    dp = [[0] * n for _ in range(k + 1)] # set 0 for rows=3, cols=n
    
    for t in range(1, k + 1):  # Try 1 to k transactions
        max_diff = -prices[0]  # best previous (profit - price)
        for d in range(1, n):
            # Option 1: Don't sell today (carry forward yesterday's profit) # (dp[t][d - 1])
            # Option 2: Sell today (prices[d] + best earlier buy) # (prices[d] + max_diff)
            dp[t][d] = max(dp[t][d - 1], prices[d] + max_diff)
            
            # Update leftover from last transaction i.e. max_diff for tomorrow # dp[t - 1][d] - prices[d]
            max_diff = max(max_diff, dp[t - 1][d] - prices[d])
    
    return dp[k][n - 1]

prices = [3, 2, 6, 8, 0, 3]
k = 2

print(maxProfit(k, prices))  # Output: 7 (Buy at 2, sell at 6, profit = 4; buy at 0, sell at 3, profit = 3)

"""
Days →
Trans ↓ 0   1   2   3   4   5
--------------------------------
0     | 0 | 0 | 0 | 0 | 0 | 0 |
1     | 0 | 0 | 4 | 6 | 6 | 6 |
2     |   |   |   |   |   |   |

Days →
Trans ↓ 0   1   2   3   4   5
--------------------------------
0     | 0 | 0 | 0 | 0 | 0 | 0 |
1     | 0 | 0 | 4 | 6 | 6 | 6 |
2     | 0 | 0 | 4 | 6 | 6 | 9 |
"""