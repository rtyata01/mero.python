# Given an array prices[] where prices[i] is the price of a stock on day i.
# An integer k representing the maximum number of transactions (buy and sell pairs).
# Find the Maximize total profit with at most k transactions.

from functools import cache

def maxProfit(k, prices):
    if not prices or k == 0:
        return 0

    n = len(prices)
    
    # Optimization: for large k, convert to unlimited transactions case
    if k >= n // 2:
        return sum(max(prices[i+1] - prices[i], 0) for i in range(n - 1))

    @cache
    def compute_max_profit(day, transactions_left, holding):
        if day == n or transactions_left == 0:
            return 0

        if holding:
            # Option 1: Sell today
            sell = prices[day] + compute_max_profit(day + 1, transactions_left - 1, 0)
            # Option 2: Hold and do nothing
            hold = compute_max_profit(day + 1, transactions_left, 1)
            return max(sell, hold)
        else:
            # Option 1: Buy today
            buy = -prices[day] + compute_max_profit(day + 1, transactions_left, 1)
            # Option 2: Skip and do nothing
            skip = compute_max_profit(day + 1, transactions_left, 0)
            return max(buy, skip)

    # Start at day 0, with k transactions left, and not holding a stock as, there is no stock and you need to buy first.
    return compute_max_profit(0, k, 0)

# Time complexity:
    # unlimited transactions: o(n), where k > n // 2
    # limited transactions: o(nk), where n is the number of days and k is the transactions count.
# Space Complexity: O(nk)

prices = [3, 2, 6, 8, 0, 3]
k = 1
print(f"Max profit: ", maxProfit(k, prices))  # Output: 7 (Buy at 2, sell at 8, profit = 6)

prices = [3, 2, 6, 8, 0, 3]
k = 2
print(f"Max profit: ", maxProfit(k, prices))  # Output: 7 (Buy at 2, sell at 6, profit = 4; buy at 0, sell at 3, profit = 3)

