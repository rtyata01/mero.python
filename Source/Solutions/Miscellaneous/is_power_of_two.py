def is_power_of_two(n):
    if n <= 0:
        return False
    return n & (n - 1) == 0

def is_power_two(n):
    power = 1
    while power <= n:
        if power == n:
            return True
        power = power * 2
    return False

print(is_power_of_two(8))   # True
print(is_power_of_two(6))   # False
print(is_power_of_two(1))   # True
print(is_power_of_two(0))   # False

# Example: 4 = 100, 4 - 1 = 011 → 100 & 011 = 000  (bit operator)

print(is_power_two(8))   # True
print(is_power_two(6))   # False
print(is_power_two(1))   # True
print(is_power_two(0))   # False