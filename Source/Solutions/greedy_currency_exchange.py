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
    
def main():
    denominations = [25, 10, 5, 1] # quater, nikel, dime, cent
    amount = 56 # Amount in cents
    
    change = get_change(denominations, amount)
    
    print(f"Change for {amount} cents:")
    for coin, count in change.items():
        print(f"{count} x {coin} cents")
        
if __name__ == "__main__":
    main()