# a subsequende of a string is a new string generated from the orignal string with some characters, 
# or all character without changing the relative order of the remaining characters

class Solution:
    def longest_common_subsequence(self, word1, word2, p1=0, p2=0, cache=None):
        if cache is None:
            cache = {}

        if p1 == len(word1) or p2 == len(word2):
            return ""

        if (p1, p2) in cache:
            return cache[(p1, p2)]

        if word1[p1] == word2[p2]:
            result = word1[p1] + self.longest_common_subsequence(word1, word2, p1 + 1, p2 + 1, cache)
        else:
            subseq1 = self.longest_common_subsequence(word1, word2, p1 + 1, p2, cache)
            subseq2 = self.longest_common_subsequence(word1, word2, p1, p2 + 1, cache)
            result = subseq1 if len(subseq1) > len(subseq2) else subseq2

        cache[(p1, p2)] = result
        return result


# Example usage:
sol = Solution()
longest_subseq = sol.longest_common_subsequence("1bcdddde", "2cddeffff")
print(f"Longest common subsequence: '{longest_subseq}' lenght: {len(longest_subseq)}")

longest_subseq = sol.longest_common_subsequence("abc", "abc")
print(f"Longest common subsequence: '{longest_subseq}' lenght: {len(longest_subseq)}")

longest_subseq = sol.longest_common_subsequence("aaaa", "bbb")
print(f"Longest common subsequence: '{longest_subseq}' lenght: {len(longest_subseq)}")




