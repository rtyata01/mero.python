# Problem: Given a list of intervals, merge all overlapping intervals.

def merge(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for curr in intervals[1:]:
        prev = merged[-1]
        if curr[0] <= prev[1]:
            prev[1] = max(prev[1], curr[1])
        else:
            merged.append(curr)
    
    return merged

# Time Complexity: O(n log n)
# sort: O(n log n)
# merge: O(n)
# Space Complexity: O(n)

 
# Tests
 
# Case 1: Basic overlapping intervals
intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals1))  # Expected: [[1, 6], [8, 10], [15, 18]]

# Case 2: No overlapping intervals
intervals2 = [[1, 2], [3, 4], [5, 6]]
print(merge(intervals2))  # Expected: [[1, 2], [3, 4], [5, 6]]

# Case 3: Fully nested intervals
intervals3 = [[1, 10], [2, 3], [4, 8]]
print(merge(intervals3))  # Expected: [[1, 10]]

# Case 4: Adjacent intervals (end meets start)
intervals4 = [[1, 2], [2, 3], [3, 4]]
print(merge(intervals4))  # Expected: [[1, 4]]

# Case 5: Single interval
intervals5 = [[5, 7]]
print(merge(intervals5))  # Expected: [[5, 7]]

# Case 6: Empty input
intervals6 = []
print(merge(intervals6))  # Expected: []

# Case 7: Intervals with negative values
intervals7 = [[-10, -1], [-5, 0], [1, 5]]
print(merge(intervals7))  # Expected: [[-10, 0], [1, 5]]