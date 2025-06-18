# Given a string s and an integer k, 
# find the longest substring where you can replace at most k characters to make all characters in the substring the same.

from collections import defaultdict
from collections import Counter

def character_replacement(s: str, k: int) -> int:
    count = defaultdict(int) # Counter()
    max_len = 0
    max_count = 0
    left = 0

    for right, char in enumerate(s):
        count[char] += 1
        max_count = max(max_count, count[char])
        window_size = right - left + 1
        
        # Shrink the window if replacements needed exceed k
        if window_size - max_count > k:
            count[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

#"ACABD" → replace 'C' and 'B' with 'A' → "AAAA"
result = character_replacement("ACABD", 2)
print(f"Expected: 4, Replacing 2 characters, longest possible string lenght: ", result)
