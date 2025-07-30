# Hard: Design a data structure to find the median of a stream of numbers in O(1) time after adding numbers in O(log n) time.
# Find the median, after n number of inserts into an array.

# Use two heaps, 
    # max heap, to track the negative numbers.
    # min heap, to track small numbers.
# insert into max heap.
# move the largest from max heap to min heap.
# if min heap size is greater that max heap size, then pushed the smallest from min heap to max heap.
from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        self.max_heap = []  # max-heap (invert sign)
        self.min_heap = []  # min-heap

    def addNum(self, num: int) -> None:
        heappush(self.max_heap, -num)
        
        # Move the largest from max-heap to min-heap
        heappush(self.min_heap, -heappop(self.max_heap))

        # Balance the heaps
        if len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2

# Time Complexity: addNum = O(log n) + findMedian = O(1)
# Space Complexity: O(n)

mf = MedianFinder()
mf.addNum(1)
print(mf.findMedian())  # Output: 1
# Only one number added, median is that number itself.

mf.addNum(5)
mf.addNum(3)
mf.addNum(8)
print(mf.findMedian())  # Output: 4.0
# Numbers: [1, 3, 5, 8], median is (3 + 5) / 2 = 4.0

mf.addNum(2)
print(mf.findMedian())  # Output: 3
# Numbers: [1, 2, 3, 5, 8], median is the middle element 3


def find_median_after_inserts(nums):
    nums.sort()                                 # O(n log n)
    n = len(nums)
    mid = n // 2
    
    if n % 2 == 1:
        return nums[mid]                        # Odd length -> middle element
    else:
        return (nums[mid - 1] + nums[mid]) / 2  # Even length -> average of middle two
    
print(f"Expected median: 1, Computed median: {find_median_after_inserts([1])}")
print(f"Expected median: 4.0, Computed median: {find_median_after_inserts([1, 3, 5, 8])}") 
print(f"Expected median: 3, Computed median: {find_median_after_inserts([1, 2, 3, 5, 8])}") 