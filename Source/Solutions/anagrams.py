from collections import Counter

class Solution:
    def is_anagram(self, source: str, target: str) -> bool:
        counter_s = Counter(source)
        counter_t = Counter(target)
        return counter_s == counter_t

    def is_anagram_sort(self, source: str, target: str) -> bool:
        s = sorted(source)
        t = sorted(target)
        return s == t

sol = Solution()

# Time complexity O(n)
print(sol.is_anagram("listen", "silent"))  # True
print(sol.is_anagram("hello", "bello"))    # False

# Time complexity O(n log n)
print(sol.is_anagram_sort("listen", "silent"))  # True
print(sol.is_anagram_sort("hello", "bello"))    # False