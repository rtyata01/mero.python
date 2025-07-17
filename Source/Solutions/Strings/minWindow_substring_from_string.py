# Hard: Find the smallest substring in S that contains all characters of T (including duplicates).

from collections import Counter, defaultdict

def shortest_substring(source, target):
    if not source or not target:
        return ""
    
    target_count = Counter(target)
    window_counts = defaultdict(int)
    
    min_len = float('inf')
    min_window = (0, 0)
    formed = 0
    left = 0

    for right, char in enumerate(source):
        if char in target_count:
            window_counts[char] += 1
            if window_counts[char] == target_count[char]:
                formed += 1

        while formed == len(target_count):
            if right - left < min_len:
                min_len = right - left
                min_window = (left, right)

            left_char = source[left]
            if left_char in target_count:
                window_counts[left_char] -= 1
                if window_counts[left_char] < target_count[left_char]:
                    formed -= 1
            left += 1

    if min_len == float('inf'):
        return ""
    
    start, end = min_window
    return "".join(source[start:end+1])

# Time Complexity: O(|S| + |T|), where S and T are the input strings.
# Space Complexity: O(|S| + |T|) for the hash maps.

source = "ADOBECODEBANC"
target = "ABC"
print(f"minWindow substring: {shortest_substring(source, target)} from source: {source} with target: {target}")

source = "ADOBECODEBANC"
target = "ABE"
print(f"minWindow substring: {shortest_substring(source, target)} from source: {source} with target: {target}")