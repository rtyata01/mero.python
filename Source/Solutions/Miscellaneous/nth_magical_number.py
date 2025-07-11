# Given the three integers n, a, and b, return the nth magical number modulo  + 7 as it can be very large.
# A positive integer is called magical if it is divisible by either a or b.

# magical_count(x) = x//a + x//b - x//lcm(a,b)
# Set low = min(a, b) and high = n * min(a, b) — the n-th magical number must lie within this range.
# Use binary search to find the smallest x such that the count of magical numbers ≤ x is at least n.

import math

def nth_magical_number(n: int, a: int, b: int) -> int:
    MOD = 10**9 + 7
    
    def lcm(x, y):
        return x * y // math.gcd(x, y)
    
    low = min(a, b)
    high = n * low
    lcm_ab = lcm(a, b)
    
    while low < high:
        mid = (low + high) // 2
        count = mid // a + mid // b - mid // lcm_ab
        if count < n:
            low = mid + 1
        else:
            high = mid
    
    return low % MOD

# (min) 2, 4, 6, 8 , (min)*n = 2*5 = 10
print(nth_magical_number(5, 2, 4))  # Output: 10
# (min) 2, 3, 4, 6, (min)*n = 2*4 = 8
print(nth_magical_number(4, 2, 3))  # Output: 6