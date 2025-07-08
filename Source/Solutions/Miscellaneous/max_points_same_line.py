# Find the maximum number of points that lie on the same straight line.
from collections import defaultdict
from math import gcd

def max_points(points):
    n = len(points)
    if n <= 2:  # 2 points → always lie on a straight line (only one line passes through two points).
        return n  

    max_result = 0
    for i, (x1, y1) in enumerate(points):
        slope_count = defaultdict(int)
        duplicates = 0
        cur_max = 0

        for j in range(i + 1, len(points)):
            x2, y2 = points[j]
            
            dx, dy = x2 - x1, y2 - y1
            
            if dx == 0 and dy == 0:
                duplicates += 1
                continue

            g = gcd(dx, dy)  # greatest common divisor of dx and dy.
            dx = dx // g
            dy = dy // g
            
             # Normalize slope to avoid direction ambiguity. (-2,-1) have same slope as (2,1)
            if dx < 0:
                dx, dy = -dx, -dy
            elif dx == 0:  # horizontal line # (0, 5) vs (0, -5) vs (0, 1)
                dy = 1
            elif dy == 0:  # vertical line #(3, 0) vs (-1, 0) vs (1, 0) 
                dx = 1
                
            slope = (dy, dx)
            slope_count[slope] += 1
            cur_max = max(cur_max, slope_count[slope])

        max_result = max(max_result, cur_max + duplicates + 1)

    return max_result

points = [(1,1), (2,2), (3,3), (4,4), (0,0), (1,0), (2,1)]
print(f"Expected: 5, Computed: ", max_points(points)) 

points = [(1,1), (3,0), (2,4)]
print(f"Expected: 2, Computed: ", max_points(points)) 
