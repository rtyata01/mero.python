# Problem: Given a string s, find the length of the longest substring without repeating characters.
# Use Sliding Window

def length_of_longest_substring_efficient(source):
    seen = {}
    left = max_len = 0
    max_start = 0
    for right, char in enumerate(source):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1

        seen[char] = right
        if right - left + 1 > max_len:
            max_len = right - left + 1
            max_start = left
    
    longest_substring = source[max_start:max_start + max_len]
    print(f"Original string: {source}, Max Length: {max_len}, Longest Substring: {longest_substring}")    
    return max_len

# Time Complexity: O (n)
# Space Complexity: O (min(n, m)) where m is unique characters, worste case n=m, so O(n)

def length_of_longest_substring(source):
    char_set = set()
    left = max_len = 0
    max_start = 0

    for right, char in enumerate(source):
        while char in char_set:
            char_set.remove(source[left])
            left += 1
            
        char_set.add(char)
        
        if right - left + 1 > max_len:
            max_len = right - left + 1
            max_start = left

    longest_substring = source[max_start:max_start + max_len]            
    print(f"Original string: {source}, Max Length: {max_len}, Longest Substring: {longest_substring}")
    return max_len

# Time Complexity: O (n)
# Space Complexity: O (min(n, m)) where m is unique characters, worste case n=m, so O(n)


def length_of_longest_substring_naive(source: str) -> int:
    n = len(source)
    max_len = 0
    max_start = 0

    # Check all substrings
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if source[j] in seen:  # Duplicate found → stop expanding
                break
            seen.add(source[j])
            if j - i + 1 > max_len:
                max_len = j - i + 1
                max_start = i

    longest_substring = source[max_start:max_start + max_len]
    print(f"Original string: {source}, Max Length: {max_len}, Longest Substring: {longest_substring}")
    return max_len

# Time Complexity: O(n^2)
# Space Complexity: O(n)

# Tests
length_of_longest_substring_efficient("")
length_of_longest_substring_efficient("aaaaa")
length_of_longest_substring_efficient("abcdef")
length_of_longest_substring_efficient("bacadefghhh")
length_of_longest_substring_efficient("a1!b2@c3#")
length_of_longest_substring_efficient("abcdefffff")
length_of_longest_substring_efficient("abcabcbb")

print("\n")
length_of_longest_substring("")
length_of_longest_substring("aaaaa")
length_of_longest_substring("abcdef")
length_of_longest_substring("bacadefghhh")
length_of_longest_substring("a1!b2@c3#")
length_of_longest_substring("abcdefffff")
length_of_longest_substring("abcabcbb")