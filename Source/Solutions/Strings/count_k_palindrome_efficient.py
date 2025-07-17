#  Counts how many palindromes have some permutation divisible by k

from itertools import permutations

def generate_palindromes(n):
    half = (n + 1) // 2
    start = 10**(half - 1)
    end = 10**half
    palindromes = []

    for first_half in range(start, end):
        first_half_str = str(first_half)
        if n % 2 == 0:
            full = first_half_str + first_half_str[::-1]    # reverse string, 12[::-1] = 1221
        else:
            full = first_half_str + first_half_str[-2::-1]  # reverse from second last char, 12[-2::-1] = 121 
        palindromes.append(full)
    return palindromes

def count_good_numbers(n, k):
    palindromes = generate_palindromes(n)
    good_number_set = set()

    for pal in palindromes:
        if int(pal) % k != 0:
            continue
        
        # Count how many n-digit numbers can be formed using digits of this pal
        unique_perms = set(permutations(pal))
        for perm in unique_perms:
            if perm[0] == '0':
                continue
            candidate = ''.join(perm)    
            good_number_set.add(candidate)
            print(f"Good Number: {candidate}")
        
    return len(good_number_set)

# Example
n = 3
k = 5
print(count_good_numbers(n, k))
