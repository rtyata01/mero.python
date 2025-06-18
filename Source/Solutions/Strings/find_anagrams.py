from collections import Counter

def find_anagrams(s: str, p: str):
    p_len = len(p)
    p_count = Counter(p)
    s_count = Counter()
    result = []
    
    for i, char in enumerate(s):
        s_count[char] += 1
        # print(f"Iteration: {i} ...............")
        # print(f"Processing Value: {s[i]}, scount= {s_count}")
        
        if i >= p_len:
            left_char = s[i - p_len]
            if s_count[left_char] == 1:
                del s_count[left_char]
                # print(f"Remove Value: {left_char}, count: {s_count}")
            else: 
                s_count[left_char] -=1
                # print(f"Decrease Value: {left_char}}, count: {s_count}")
        
        if s_count == p_count:
            # print(f"scount: {s_count}, pcount= {p_count}")
            start_index = i - p_len + 1
            result.append(start_index)
            print(f"Found Anagram: {s[start_index: start_index + p_len]}")
    
    return result

# The final result is [0, 6], as s[0:3] = 'cba' and s[6:9] = 'bac' are both anagrams of p = "abc".
print(find_anagrams("cbaebabacd", "abc"))
