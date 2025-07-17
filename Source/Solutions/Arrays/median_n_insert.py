# Hard: Design a data structure to find the median of a stream of numbers in O(1) time after adding numbers in O(log n) time.
# Find the median, after n number of inserts into an array.

from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap (store negatives)
        self.large = []  # min-heap

    def addNum(self, num):
        # Push onto small heap first (as negative for max-heap behavior)
        heappush(self.small, -num)

        # Ensure every number in small is <= every number in large
        if self.large and (-self.small[0] > self.large[0]):
            val = -heappop(self.small)
            heappush(self.large, val)

        # Balance sizes: small can only have 1 more element than large
        if len(self.small) > len(self.large) + 1:
            val = -heappop(self.small)
            heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heappop(self.large)
            heappush(self.small, -val)

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2

# Time Complexity: addNum = o(logn) + findMedian = o(1)
# Space Complexity: o(n)

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