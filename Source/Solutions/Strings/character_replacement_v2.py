# Given a string s and an integer k, 
# find the longest substring where you can replace at most k characters to make all characters in the substring the same.

from collections import defaultdict

def character_replacement_with_result(s: str, k: int):
    count = defaultdict(int)
    max_count = 0
    max_len = 0
    left = 0
    
    start_index = 0  # To track the starting index of the longest window
    max_count_char = ''  # The dominant character to fill with

    for right, char in enumerate(s):
        count[char] += 1
        if count[char] > max_count:
            max_count = count[char]
            max_count_char = char  # Update the dominant char

        window_size = right - left + 1
        if window_size - max_count > k:
            count[s[left]] -= 1
            left += 1

        if right - left + 1 > max_len:
            max_len = right - left + 1
            start_index = left

    # Build the final result string using the dominant character
    result_string = s[start_index:start_index + max_len]
    print(f"original string: ", result_string)
    
    replaced_string = max_count_char * max_len
    return max_len, replaced_string


#"ACABD" → replace 'C' and 'B' with 'A' → "AAAA"
length, result = character_replacement_with_result("ACABD", 2)
print(f"Expected: 4, Replacing 2 characters, longest possible string lenght: {length}, replaced string: {result}")

length, result = character_replacement_with_result("AABABBD", 2)
print(f"Expected: 5, Replacing 2 characters, longest possible string lenght: {length}, replaced string: {result}")

length, result = character_replacement_with_result("ABCABBD", 2)
print(f"Expected: 5, Replacing 2 characters, longest possible string lenght: {length}, replaced string: {result}")