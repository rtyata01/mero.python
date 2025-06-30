import random
import bisect

class WeightedRandomPicker:
    def __init__(self, weights):
        self.prefix_sums = []
        self.min = float('inf')
        self.total = 0
        for weight in weights:
            self.total += weight # Store total sum for random range
            self.prefix_sums.append(self.total)
            self.min = min(self.min, weight) # Store the min weight.

    def pickIndex(self):
        # Pick random number between min and total inclusive.
        target = random.randint(self.min, self.total)
        
        # Find first prefix >= target → gives correct index
        prefix_sum_index = bisect.bisect_left(self.prefix_sums, target) 
        return prefix_sum_index


# Servers with capacity weights
servers = ["A", "B", "C"]
weights = [1, 3, 2] # weights for indexes 0 (1/6 = 16.6%), 1(3/6 = 50%), 2 (2/6 = 33.3)

picker = WeightedRandomPicker(weights)

# Pick a server based on load capacity
for i in range(10):
    index = picker.pickIndex()
    print(f"Selected server: {servers[index]}")

# target = random number in [1, 6]
# prefix_sums:     [1, 4, 6]
# value ranges:    [1] [2,3,4] [5,6]
# indices:         0     1    2   
# So if target = 3, we binary search:
# Is 3 ≤ 1? → no
# Is 3 ≤ 4? → yes → index = 1