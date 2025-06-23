# Greed Algorithm fail results larger number of coins, so it is not optimal in some cases.

def get_change(denominations, amount):
    result = {}
    
    for coin in denominations:
        if amount <= 0:
            break
        
        count = amount // coin
        if count > 0:
            amount -= count * coin
            result[coin] = count
        
    return result
    
# Example
denominations = [9, 6, 1]
amount = 12 # Amount in cents

result = get_change(denominations, amount)
print(f"Change for {amount} cents:", result)

# denominations = [9, 6, 1]
# amount = 12
# Greed output = {9:1, 1:3}  # total coins = 4
# Optimal solution = {6:2} # total coins = 2

denominations = [1, 9, 6]
amount = 12 # Amount in cents

result = get_change(denominations, amount)
print(f"Change for {amount} cents:", result)
    
