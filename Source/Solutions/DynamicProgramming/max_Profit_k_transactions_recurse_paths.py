# Find the maximum profits, for at most K transactions. 
# Each trasaction refers 1 buy and 1 sell activity.

from functools import cache

def maxProfit(k, prices):
    n = len(prices)
    if not prices or k == 0:
        return 0, []

    # Optimization for unlimited transactions
    if k >= n // 2:
        profit = 0
        transactions = []
        for i in range(0, n-1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]
                transactions.append((prices[i], prices[i + 1]))
        return profit, transactions

    @cache
    def compute_max_profit(day, transactions_left, holding):
        if day == n or transactions_left == 0:
            return 0, []

        if holding:
            # Option 1: Sell today
            sell_profit, sell_path = compute_max_profit(day + 1, transactions_left - 1, 0)
            sell_profit += prices[day]

            # Option 2: Hold
            hold_profit, hold_path = compute_max_profit(day + 1, transactions_left, 1)

            if sell_profit > hold_profit:
                return sell_profit, [(None, prices[day])] + sell_path
            else:
                return hold_profit, hold_path

        else:
            # Option 1: Buy today
            buy_profit, buy_path = compute_max_profit(day + 1, transactions_left, 1)
            buy_profit -= prices[day]

            # Option 2: Skip
            skip_profit, skip_path = compute_max_profit(day + 1, transactions_left, 0)

            if buy_profit > skip_profit:
                return buy_profit, [(prices[day], None)] + buy_path
            else:
                return skip_profit, skip_path

    profit, raw_path = compute_max_profit(0, k, 0)
    print(f"Raw Paths: {raw_path}")

    # Post-process raw_path to match buys with sells
    transactions = []
    buy_price = None
    for buy, sell in raw_path:
        if buy is not None:
            buy_price = buy
        if sell is not None and buy_price is not None:
            transactions.append((buy_price, sell))
            buy_price = None

    return profit, transactions

# Example usage:
prices = [3, 2, 6, 8, 0, 3]
k = 2
profit, transactions = maxProfit(k, prices)

print(f"Maximum Profit: {profit}")
for buy, sell in transactions:
    print(f"Buy at {buy}, Sell at {sell}, max profit = {sell - buy}")
