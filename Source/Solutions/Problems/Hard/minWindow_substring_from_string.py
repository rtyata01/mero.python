# Hard: Find the smallest substring in S that contains all characters of T (including duplicates).

from collections import Counter, defaultdict

def shortest_substring(source, target):
    if not source or not target:
        return ""
    
    target_freq = Counter(target)
    window_freq = defaultdict(int)
    
    min_len = float('inf')
    left = 0
    start = 0
    formed = 0

    for right, char in enumerate(source):
        if char in target_freq:
            window_freq[char] += 1
            if window_freq[char] == target_freq[char]:
                formed += 1

        while formed == len(target_freq):
            # Update minimum window
            window_size = right - left + 1 
            if window_size < min_len:
                min_len = window_size
                start = left
                                    
            # Shrink from left
            left_char = source[left]
            if left_char in target_freq:            
                window_freq[left_char] -= 1
                if window_freq[left_char] < target_freq[left_char]:
                    formed -= 1
            left += 1
            
    return source[start:start + min_len] if min_len != float('inf') else ""

# Time Complexity: O(n + m), where n is souce length and m is target lenght.
# Space Complexity: O(m) for the hash maps.

source = "ADOBECODEBANC"
target = "ABC"
print(f"minWindow substring: {shortest_substring(source, target)} from source: {source} with target: {target}")

source = "ADOBECODEBANC"
target = "ABE"
print(f"minWindow substring: {shortest_substring(source, target)} from source: {source} with target: {target}")