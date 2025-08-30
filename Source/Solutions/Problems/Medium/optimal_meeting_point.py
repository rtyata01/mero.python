# Problem: Given a list of points (people), find a point (x, y) such that the sum of Manhattan distances from all points to (x, y) is minimized.
# The optimal meeting point is at the median of the x-coordinates and y-coordinates of the points.
# The sum of absolute differences is minimized at the median.

def min_total_manhattan_distance(points):
    if not points:
        return None, None
    
    # Separate x and y coordinates
    xs = sorted([x for x, _ in points])
    ys = sorted([y for _, y in points])

    # Find medians
    mid_x = xs[len(xs) // 2]
    mid_y = ys[len(ys) // 2]

    # Calculate total distance to the median point
    total_distance = sum(abs(x - mid_x) + abs(y - mid_y) for x, y in points)

    return (mid_x, mid_y), total_distance

# Time Complexity: O(n log n)
    # Sorting: O(n log n)
    # Distance calculation: O(n)
# Space complexity: O(n) (to store sorted coordinate lists).

# Naive, less efficient solution
# loop through all points, and find the minimal distance.
def min_total_manhattan_distance_naive(points):
    if not points:
        return None, None

    best_point = None
    min_distance = float("inf")

    for candidate in points:
        cx, cy = candidate
        total_distance = sum(abs(x - cx) + abs(y - cy) for x, y in points)

        if total_distance < min_distance:
            min_distance = total_distance
            best_point = candidate

    return best_point, min_distance

# Time complexity: O(n^2)
# Space complexity: O(1)

points = [(0, 0), (2, 4), (3, 3)]
meeting_point, distance = min_total_manhattan_distance(points)
print("Optimal meeting point:", meeting_point)
print("Total Manhattan distance:", distance)


points = [(1, 1), (1, 1), (1, 1)]
meeting_point, distance = min_total_manhattan_distance(points)
print("Optimal meeting point:", meeting_point)
print("Total Manhattan distance:", distance)

points = [(0, 0), (2, 0), (4, 0)]
meeting_point, distance = min_total_manhattan_distance(points)
print("Optimal meeting point:", meeting_point)
print("Total Manhattan distance:", distance)
