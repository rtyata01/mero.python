# Problem: Given a list of intervals, merge all overlapping intervals.

# For naive approach, use brute force i.e. compare each pair with all other pairs and merge.
# for i in range(len(intervals)):
    # for j in range(i+1, len(intervals)):

def merge(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for curr in intervals[1:]:
        prev = merged[-1]
        if prev[1] > curr[0]:
            prev[1] = max(prev[1], curr[1])
        else:
            merged.append(curr)
    
    return merged

# Time Complexity: O(n log n)
# sort: O(n log n)
# merge: O(n)
# Space Complexity: O(n)

def merge_inplace(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    i = 0
    for j in range(1, len(intervals)):
        if intervals[i][1] >= intervals[j][0]:
            intervals[i][1] = max(intervals[i][1], intervals[j][1])
        else:
            i += 1
            intervals[i] = intervals[j]
    
    return intervals[:i+1]

# Time Complexity: O(n log n)
# Space Complexity: O(1)

# Tests

test_cases = [
    [[1, 3], [2, 6], [8, 10], [15, 18]], # Basic overlapping intervals [[1, 6], [8, 10], [15, 18]]
    [[1, 2], [3, 4], [5, 6]], # No overlapping intervals [[1, 2], [3, 4], [5, 6]]
    [[1, 10], [2, 3], [4, 8]], # Fully nested intervals [[1, 10]]
    [[1, 2], [2, 3], [3, 4]], # Adjacent intervals (end meets start) [[1, 4]]
    [[5, 7]], # Single interval [[5, 7]]
    [[-10, -1], [-5, 0], [1, 5]] # Intervals with negative values  [[-10, 0], [1, 5]]
]

for input in test_cases:
     print(merge(input))
     print(merge_inplace(input)) 