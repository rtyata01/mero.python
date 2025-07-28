# Problem: Given a list of points (people), find a point (x, y) such that the sum of Manhattan distances from all points to (x, y) is minimized.
# The optimal meeting point is at the median of the x-coordinates and y-coordinates of the points.
# The sum of absolute differences is minimized at the median.

# Naive, less efficient solution
# find min and max for x and y coordinates.
# loop x from min_x, max_y + 1
# inner loop y from min_y, max_y + 1
# evaluate the total distance, for all points and find the min total.

def min_total_manhattan_distance(points):
    if not points:
        return None, None
    
    # Separate x and y coordinates
    xs = sorted([x for x, y in points])
    ys = sorted([y for x, y in points])

    # Find medians
    mid_x = xs[len(xs) // 2]
    mid_y = ys[len(ys) // 2]

    # Calculate total distance to the median point
    total_distance = sum(abs(x - mid_x) + abs(y - mid_y) for x, y in points)

    return (mid_x, mid_y), total_distance

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
