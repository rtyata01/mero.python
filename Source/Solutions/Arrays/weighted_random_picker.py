import random
import bisect

class WeightedRandomPicker:
    def __init__(self, w):
        self.prefix_sums = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sums.append(total)
        self.total = total  # Store total sum for random range

    def pickIndex(self):
        # Pick random number between 1 and total  6
        target = random.randint(1, self.total)
        
        # Find first prefix >= target → gives correct index
        return bisect.bisect_left(self.prefix_sums, target)


# Servers with capacity weights
servers = ["A", "B", "C"]
weights = [1, 3, 2] # weights for indices 0 (1/6 = 16.6%), 1(3/6 = 50%), 2 (2/6 = 33.3)

picker = WeightedRandomPicker(weights)

# Pick a server based on load capacity
for i in range(10):
    selected = servers[picker.pickIndex()]
    print(f"Selected server: {selected}")

# target = random number in [1, 6]
# prefix_sums:     [1, 4, 6]
# value ranges:    [1] [2,3,4] [5,6]
# indices:         0     1       
# So if target = 3, we binary search:
# Is 3 ≤ 1? → no
# Is 3 ≤ 4? → yes → index = 1