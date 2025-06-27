import random
import bisect

class WeightedRandomPicker:
    def __init__(self, w):
        self.prefix_sums = []
        total = 0
        min = float('inf')
        for weight in w:
            total += weight
            self.prefix_sums.append(total)
            if weight < min:
                min = weight
        self.total = total  # Store total sum for random range
        self.min = min # Store the min weight.

    def pickIndex(self):
        # Pick random number between min and total inclusive.
        target = random.randint(self.min, self.total)
        #print(f"Random number: {target}")
        
        # Find first prefix >= target → gives correct index
        prefix_sum_index = bisect.bisect_left(self.prefix_sums, target) 
        #print(f"Prefix sum index: {prefix_sum_index}")
        return prefix_sum_index


# Servers with capacity weights
servers = ["A", "B", "C"]
weights = [1, 3, 2] # weights for indexes 0 (1/6 = 16.6%), 1(3/6 = 50%), 2 (2/6 = 33.3)

picker = WeightedRandomPicker(weights)

# Pick a server based on load capacity
for i in range(10):
    selected = servers[picker.pickIndex()]
    print(f"Selected server: {selected}")

# target = random number in [1, 6]
# prefix_sums:     [1, 4, 6]
# value ranges:    [1] [2,3,4] [5,6]
# indices:         0     1    2   
# So if target = 3, we binary search:
# Is 3 ≤ 1? → no
# Is 3 ≤ 4? → yes → index = 1