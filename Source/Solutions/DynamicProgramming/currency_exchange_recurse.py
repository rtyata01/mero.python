class Solution:
    def get_min_change_all(self, denominations, amount, cache=None):
        if cache is None:
            cache = {}

        # Base cases
        if amount == 0:
            return [[]]  # one way: no coins
        
        if amount < 0:
            return []  # no way

        if amount in cache:
            return cache[amount]

        min_coins = float('inf')
        all_ways = []

        for coin in denominations:
            remainder = amount - coin
            sub_ways = self.get_min_change_all(denominations, remainder, cache)

            for way in sub_ways:
                new_way = way + [coin]

                if len(new_way) < min_coins:
                    min_coins = len(new_way)
                    all_ways = [new_way]  # found a smaller combo, reset
                elif len(new_way) == min_coins:
                    all_ways.append(new_way)  # same size, add to list

        cache[amount] = all_ways
        return all_ways

sol = Solution()
denominations = [1, 3, 4]
amount = 6

all_min_combinations = sol.get_min_change_all(denominations, amount)

print(f"All minimum coin combinations to make {amount}:")
for combo in all_min_combinations:
    print(combo)
print(f"Number of minimum combinations: {len(all_min_combinations[0])}")