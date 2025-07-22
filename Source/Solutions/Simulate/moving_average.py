# Implement moving average, to maintain the average of the last size elements.

from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque(maxlen=size)  # Automatically limits to size
        self.current_sum = 0.0  # Track sum for O(1) average

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.current_sum += val
        
        # If queue exceeds size, remove oldest element from sum
        if len(self.queue) > self.size:
            self.current_sum -= self.queue.popleft()
        # Return average
        return self.current_sum / min(len(self.queue), self.size)
    
    
ma = MovingAverage(3) # size 3
print(f"Moving average is {ma.next(1)} for: {ma.queue}") # output 1
print(f"Moving average is {ma.next(10)} for: {ma.queue}") # output (1 + 10) / 2 = 5.5
print(f"Moving average is {ma.next(3)} for: {ma.queue}") # output  (1 + 10 + 3) / 3 = 4.666...
print(f"Moving average is {ma.next(5)} for: {ma.queue}") # output  (10 + 3 + 5) / 3 = 6.0
