from collections import Counter

class Solution:
    def is_anagram(self, source: str, target: str) -> bool:
        return Counter(source) == Counter(target)

    def is_anagram_sort(self, source: str, target: str) -> bool:
        return sorted(source) == sorted(target)

    def is_anagram(self, source: str, target: str) -> bool:
        if len(source) != len(target):
            return False
        
        counts = [0] * 26
        for s, t in zip(source, target):   #zip combines multiple iterables into pairs or tuple.
            counts[ord(s) - 97] += 1    # ord converts char to unicode.
            counts[ord(t) - 97] -= 1
        
        return all(c == 0 for c in counts)


sol = Solution()

# Time complexity O(n + m)
print(sol.is_anagram("listen", "silent"))  # True
print(sol.is_anagram("hello", "bello"))    # False

# Time complexity O(n log n + m long m)
print(sol.is_anagram_sort("listen", "silent"))  # True
print(sol.is_anagram_sort("hello", "bello"))    # False