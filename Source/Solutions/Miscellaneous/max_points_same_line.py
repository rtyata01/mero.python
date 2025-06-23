# Find the maximum number of points that lie on the same straight line.
from collections import defaultdict
from math import gcd

def max_points(points):
    n = len(points)
    if n <= 2:  # 2 points → always lie on a straight line (only one line passes through two points).
        return n  

    max_result = 0
    for i in range(n):
        slopes = defaultdict(int)
        duplicates = 0
        cur_max = 0
        x1, y1 = points[i]

        for j in range(n):
            if i == j:
                continue

            x2, y2 = points[j]

            dx = x2 - x1
            dy = y2 - y1

            if dx == 0 and dy == 0:
                duplicates += 1
                continue

            g = gcd(dx, dy)  # greatest common divisor of dx and dy.
            slope = (dy // g, dx // g)

            # Normalize slope to avoid direction ambiguity
            if slope[1] < 0:
                slope = (-slope[0], -slope[1])

            slopes[slope] += 1
            cur_max = max(cur_max, slopes[slope])

        max_result = max(max_result, cur_max + duplicates + 1)

    return max_result

points = [(1,1), (2,2), (3,3), (4,4), (0,0), (1,0), (2,1)]
print(max_points(points))  # Output: 5 (points on line y = x)


points = [(1,1), (3,0), (2,4)]
print(max_points(points))  # Output: 5 (points on line y = x)
