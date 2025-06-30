from collections import Counter

def find_anagrams(source: str, target: str):
    source = source.lower()
    target = target.lower()
    
    t_len = len(target)
    t_count = Counter(target)
    s_count = Counter()
    result = []
    
    for i, char in enumerate(source):
        s_count[char] += 1
        # print(f"Iteration: {i} ...............")
        # print(f"Processing Value: {s[i]}, scount= {s_count}")
        
        if i >= t_len:
            left_char = source[i - t_len]
            if s_count[left_char] == 1:
                del s_count[left_char]
            else: 
                s_count[left_char] -=1
        
        if s_count == t_count:
            # print(f"scount: {s_count}, tcount= {t_count}")
            start_index = i - t_len + 1
            result.append(start_index)
            print(f"Found Anagram: {source[start_index: start_index + t_len]}")
    
    if not result:
        print("No anagram found.")
        
    return result

# The final result is [0, 6], as s[0:3] = 'cba' and s[6:9] = 'bac' are both anagrams of p = "abc".
print(find_anagrams("cbaebabacd", "abc"))
print(find_anagrams("abc", "abc"))
print(find_anagrams("a", "abc"))
print(find_anagrams("CBAebabACD", "abc"))
