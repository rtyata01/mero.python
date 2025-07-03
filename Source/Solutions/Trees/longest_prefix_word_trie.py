class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = ""

class Solution:
    def longestWord(self, words):    
        root = TrieNode()
        
        # Insert all words into the Trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True
            node.word = word  # store full word at the end node

        self.longest = ""

        # DFS to find the longest word with all prefixes valid
        def dfs(node):
            if node != root and not node.is_end:
                return  # skip if prefix is not valid word

            if node.word:
                if len(node.word) > len(self.longest) or (len(node.word) == len(self.longest) and node.word < self.longest):
                    # if same length, pick the lexicographically smaller word. "apple" is "smaller" that apply in order, character e comes before y.
                    self.longest = node.word

            for ch in node.children:  # for lexicographical order comparision, you need # in sorted(node.children.keys())
                dfs(node.children[ch])

        dfs(root)
        return self.longest


"""
(root)
  └─ a (is_end=True, word="a")
      └─ p (is_end=True, word="ap")
          └─ p (is_end=True, word="app")
              └─ l (is_end=True, word="appl")
                  ├─ e (is_end=True, word="apple")
                  └─ y (is_end=True, word="apply")
"""

# Time complexity = o(w), where w  is total number of characters across all words i.e. 26.
# Trie construction:  O(W)
# DFS traversal:      O(W)
# Space complexity = o(w)

sol = Solution()
print(sol.longestWord(["a", "ap", "app", "appl", "apple", "apply"]))  # "apple"
print(sol.longestWord(["w", "wo", "wor", "worl", "world", "banana"]))  # "world"
print(sol.longestWord(["a", "ap", "app", "appl", "apple", "apples", "applied", "apply"]))  # "apples"
print(sol.longestWord(["a", "ab", "abd", "abc"]))  # "abc"