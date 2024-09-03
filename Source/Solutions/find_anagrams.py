from collections import Counter

def find_anagrams(s: str, p: str):
    s_count = Counter()
    p_count = Counter(p)
    result = []
    p_len = len(p)
    
    for i in range(len(s)):
        s_count[s[i]] += 1
        print(f"Iteration: {i} ...............")
        print(f"Processing Value: {s[i]}, scount= {s_count}")
        
        if i >= p_len:
            if s_count[s[i-p_len]] == 1:
                del s_count[s[i-p_len]]
                print(f"Remove Value: {s[i-p_len]}, count: {s_count}")
            else:
                s_count[s[i - p_len]] -=1
                print(f"Decrease Value: {s[i-p_len]}, count: {s_count}")
        
        if s_count == p_count:
            print(f"scount: {s_count}, pcount= {p_count}")
            start_index = i - p_len + 1
            result.append(start_index)
            print(f"Anagram: {s[start_index: start_index + p_len]}")
    
    return result

print(find_anagrams("cbaebabacd", "abc"))