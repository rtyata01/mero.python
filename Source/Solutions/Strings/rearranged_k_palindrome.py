# An integer x is k-palindromic (with rearrangement) if:
# You can rearrange its digits to form a palindrome.
# x is divisible by 𝑘

from collections import Counter

def can_form_palindrome(x):
    digit_counts = Counter(str(x))
    odd_counts = sum (1 for count in digit_counts.values() if count % 2 != 0)
    return odd_counts <= 1  # At most one odd count is allowed

def is_rearranged_k_palindromic(num, k):
    return num % k == 0 and can_form_palindrome(num)

# Example usage:
print(is_rearranged_k_palindromic(2020, 2))  # Should return True  # 2002
print(is_rearranged_k_palindromic(220, 2))  # Should return True  # 202
print(is_rearranged_k_palindromic(22, 2))  # Should return True  # 202
print(is_rearranged_k_palindromic(1234, 2))  # Should return False
print(is_rearranged_k_palindromic(112233, 3))  # Should return True
