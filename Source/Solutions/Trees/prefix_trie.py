 # Given a list of strings, 
 # find the longest word such that every prefix of the word is also in the list.

class TrieNode:
    def __init__(self):
        self.children = {}  # maps char to TrieNode
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # create new node if needed
            node = node.children[char]
        node.is_end_of_word = True  # mark the end of a valid word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True  # found the full prefix


# Example usage
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("bat")

# root
# ├── a
# │   └── p
# │       └── p
# │           ├── l
# │           │   └── e (end)
# │           └── (end)
# └── b
#     └── a
#         └── t (end)
# 

print(trie.search("apple"))  # True
print(trie.search("app"))    # True
print(trie.search("appl"))   # False

print(trie.starts_with("app"))  # True
print(trie.starts_with("ba"))   # True
print(trie.starts_with("cat"))  # False

# Time Complexity = O(L), lenght of the word for Insert, Search, Starts with Operations.
# Check the sorting solution unders strings folder, which is more efficient.