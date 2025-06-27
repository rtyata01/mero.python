# Greed Algorithm fail results larger number of coins, so it is not optimal in some cases.

def get_change_min_coins(denominations, amount):
    def greedy(denoms, amt):
        result = {}
        count = 0
        for coin in denoms:
            if amt <= 0:
                break
            use = amt // coin
            if use > 0:
                amt -= use * coin
                result[coin] = use
                count += use
        if amt == 0:
            return result, count
        else:
            return None, float('inf')  # Cannot make change with these denoms

    best_result = None
    min_count = float('inf')

    # Try greedy with all subsets where 0 or more largest coins are removed
    sorted_denoms = sorted(denominations, reverse=True)
    for i in range(len(sorted_denoms)):
        subset = sorted_denoms[i:]  # Try skipping largest i coins
        result, count = greedy(subset, amount)
        if count < min_count:
            min_count = count
            best_result = result

    return best_result

    
# Example
denominations = [9, 6, 1]
amount = 12 # Amount in cents

# denominations = [9, 6, 1]
# amount = 12
# Greed output = {9:1, 1:3}  # total coins = 4
# Optimal solution = {6:2} # total coins = 2

result = get_change_min_coins(denominations, amount)
print(f"Change for {amount} cents:", result)

denominations = [1, 9, 6]
amount = 12 # Amount in cents

result = get_change_min_coins(denominations, amount)
print(f"Change for {amount} cents:", result)

