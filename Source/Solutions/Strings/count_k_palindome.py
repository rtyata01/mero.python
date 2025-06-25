# Counts how many n-digit numbers can be permuted into a palindrome that is divisible by k.
# good number = number, whose permutations includes a palindrome diviisble by k.

from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def is_good_number(num_str, k):
    seen = set()
    unique_perms = set(permutations(num_str))
    for p in unique_perms:
        if p[0] == '0':
            continue
        candidate = ''.join(p)
        if candidate in seen:
            continue
        seen.add(candidate)
        if is_palindrome(candidate) and int(candidate) % k == 0:
            return True
    return False

def count_good_numbers(n, k):
    start = 10**(n-1)
    end = 10**(n)
    count = 0
    for num in range(start, end):
        if is_good_number(str(num), k):
            print(f"Good Number: {num}")
            count += 1
    return count

# Example
n = 3
k = 5
print(count_good_numbers(n, k))