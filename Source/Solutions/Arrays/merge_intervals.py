def merge_intervals(intervals):
    
    # if intervals is empty, return.
    if not intervals:
        return
    
    # sort the interval, using interval key i.e. x[0] and using anonymous function lamda x
    # time complexity of this sort will be O(n log n)
    intervals.sort(key = lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
            last_merged = merged[-1]
            if last_merged[1] >= current[0]:
                    last_merged[1] = max(last_merged[1], current[1])
            else:
                merged.append(current)
        
    return merged

# Test 
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(f"Test ----------------------------------------")
print(f"Original Input: {intervals}")
print(f"Merged output: {merge_intervals(intervals)}")

intervals = [[-2, 6], [-1, 3], [8, 10], [15, 18]]
print(f"Test ----------------------------------------")
print(f"Original Input: {intervals}")
print(f"Merged output: {merge_intervals(intervals)}") 