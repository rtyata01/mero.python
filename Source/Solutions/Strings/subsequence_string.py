def is_subsequence(s: str, t: str) -> bool:
    i = 0  # Pointer for s
    for char in t:
        if i < len(s) and s[i] == char:
            i += 1
    return i == len(s)

def is_subsequence(s: str, t: str) -> bool:
    it = iter(t)
    return all(char in it for char in s)

print(f"Expected: True, Computed: ", is_subsequence("abc", "ahbgdc"))   # True
print(f"Expected: True, Computed: ", is_subsequence("", "abc"))         # True (empty string is subsequence of any string)
print(f"Expected: True, Computed: ", is_subsequence("abc", "ahbgdcab"))   # True
print(f"Expected: False, Computed: ", is_subsequence("axc", "ahbgdc"))   # False
print(f"Expected: False, Computed: ", is_subsequence("abc", ""))        # False

