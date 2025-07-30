# a subsequence of a string is a new string generated from the orignal string with some characters, 
# or all character without changing the relative order of the remaining characters

# Top down approach
# Bottom up approach = less space O(m × n) but same time complexity.

class Solution:
    def longest_common_subsequence(self, word1, word2):
        memo = {}

        def find_subsequence(p1, p2):
            if p1 == len(word1) or p2 == len(word2):
                return ""
            if (p1, p2) in memo:
                return memo[(p1, p2)]

            if word1[p1] == word2[p2]:
                result = word1[p1] + find_subsequence(p1 + 1, p2 + 1)
            else:
                subseq1 = find_subsequence(p1 + 1, p2)
                subseq2 = find_subsequence(p1, p2 + 1)
                result = subseq1 if len(subseq1) > len(subseq2) else subseq2

            memo[(p1, p2)] = result
            return result

        return find_subsequence(0, 0)
    
# Time Complexity:	O(m × n), m and n refers length of word1 and word2
# Space Complexity:	O(m × n × k), k is length of longest common subsequence

# Example usage:
sol = Solution()
longest_subseq = sol.longest_common_subsequence("1bcdddde", "2cddeffff")
print(f"Longest common subsequence: '{longest_subseq}' lenght: {len(longest_subseq)}")

longest_subseq = sol.longest_common_subsequence("abc", "abc")
print(f"Longest common subsequence: '{longest_subseq}' lenght: {len(longest_subseq)}")

longest_subseq = sol.longest_common_subsequence("aaaa", "bbb")
print(f"Longest common subsequence: '{longest_subseq}' lenght: {len(longest_subseq)}")




