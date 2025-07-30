class Solution:
    def print_optimal_change(self, denominations, amount):
        result = self.get_min_change_all(denominations, amount)
        if not result:
             print(f"No way to make change for {amount} with denominations {denominations}")
        else:
            print(f"All minimum coin combinations to make {amount}:")
            for change in result:
                print(change)
            print(f"Number of minimum combinations: {len(result[0])}")
        
    def get_min_change_all(self, denominations, amount, memo=None):
        if memo is None:
            memo = {}

        # Base cases
        if amount == 0:
            return [[]]  # Base case: one way to make 0, using no coins  # optimize: [()]

        if amount in memo:
            return memo[amount]

        min_coins = float('inf')
        min_ways = []    # optimize: set()

        for coin in denominations:
            remainder = amount - coin
            if remainder >= 0:
                sub_ways = self.get_min_change_all(denominations, remainder, memo)
                for way in sub_ways:
                    new_way = way + [coin]   # optimize: tuple(sorted(way + (coin,)))
                    if len(new_way) < min_coins:
                        # reset, found minimal change, 
                        min_coins = len(new_way)
                        min_ways = [new_way]  
                    elif len(new_way) == min_coins:  # optimize: and new_way not in min_ways:
                        # same size, add to list
                        min_ways.append(new_way)  

        memo[amount] = min_ways
        return min_ways

# Time Complexity: O (n*A), where n is the number of coins.
    # worst case: O (n^A) i.e. exponential in amount A.
# Space Complexity: O (n*A)
    # worst case: O (n^A)

sol = Solution()
denominations = [1, 3, 4]
amount = 6
sol.print_optimal_change(denominations, amount)

denominations = [1, 9, 6]
amount = 12
sol.print_optimal_change(denominations, amount)

denominations = [10, 5, 1]
amount = 35
sol.print_optimal_change(denominations, amount)