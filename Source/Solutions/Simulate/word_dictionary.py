# Search dictionary with recursive wildcard support. 
# Search "c.t", where . can be any character and returns all matching words like like cut, cat. 

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for ch in word.lower():
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        def dfs(i, node):
            if i == len(word):
                return node.is_end
            ch = word[i].lower()
            if ch == '.':
                return any(dfs(i + 1, child) for child in node.children.values())
                # for child in node.children.values():
                #    if dfs(i+1, child):
                #        return True
                # return False
            if ch not in node.children:
                return False
            return dfs(i + 1, node.children[ch])
        
        return dfs(0, self.root)

    def find_matching_words(self, word):
        results = []
        
        def dfs(i, node, path):
            if i == len(word):
                results.append("".join(path))
                return
            
            ch = word[i].lower()
            if ch == '.':
                for child_ch, child_node in node.children.items():
                    dfs(i+1, child_node, path + [child_ch])
            elif ch in node.children:
                dfs(i + 1, node.children[ch], path + [ch])
        
        dfs(0, self.root, [])
        return results


wordDictionary = WordDictionary()
wordDictionary.addWord("cat")
wordDictionary.addWord("cut")
wordDictionary.addWord("cup")
wordDictionary.addWord("dog")

print(f"Search [c..] results: ", wordDictionary.search("c.."))
print(f"Search [c..] results: ", wordDictionary.find_matching_words("c.."))

print(f"Search [cU.] results: ", wordDictionary.search("cU."))
print(f"Search [cU.] results: ", wordDictionary.find_matching_words("cU."))

print(f"Search [D.g] results: ", wordDictionary.search("D.g"))
print(f"Search [D.g] results: ", wordDictionary.find_matching_words("D.g"))

print(f"Search [b.g] results: ", wordDictionary.search("b.g"))
print(f"Search [b.g] results: ", wordDictionary.find_matching_words("b.g"))
