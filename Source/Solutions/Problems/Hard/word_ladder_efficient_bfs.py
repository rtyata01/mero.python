# Hard: Find all shortest transformation sequences from beginWord to endWord.
# Transform one word to another by changing a letter at a time, using a dictionary.

from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, words: list) -> list:
        if beginWord == endWord:
            return [[beginWord]]
        
        wordset = set(words)
        if endWord not in wordset:
            return []
    
        # Create an adjacency list where each word is linked to words, with one letter or character different
        adj = defaultdict(list)
        for word in wordset:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]  # For example, word hit have pattern *it, h*t, hi*, 
                adj[pattern].append(word)
        
        # BFS to find the shortest paths
        result = []
        queue = deque([(beginWord, [beginWord])]) # (word, path)
        visited = set([beginWord])
        found = False
        
        while queue and not found:
            level_visited = set()
            for _ in range(len(queue)):
                word, path = queue.popleft()
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    for neighbor in adj[pattern]:  # adj.get(pattern, []):
                        if neighbor == endWord:
                            result.append(path + [endWord])
                            found = True
                        if neighbor not in visited:
                            level_visited.add(neighbor)
                            queue.append((neighbor, path + [neighbor]))
            visited.update(level_visited)
        
        return result

# Time Complexity: O(N * L * M)
    # Dictionary: O(N * L), where N is the unique number of words and L is the length of each words.
    # BFS Search: O(N * L * M), where M is the number of neighbors per pattern.
# Space Complexity: O(N * L)
    # visist set = O(N), where N is the unique number of words.
    # queue and results = O (N * L), number of shortest paths and length of each paths.

# Example Usage
sol = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
result = sol.findLadders(beginWord, endWord, wordList)
print(f"result = {result}")

# adj_list
#{
#  "*ot": ["hot", "dot", "lot"],
#  "h*t": ["hot"],
#  "ho*": ["hot"],
#  "d*t": ["dot"],
#  "do*": ["dot", "dog"],
#  "*og": ["dog", "log", "cog"],
#  "d*g": ["dog"],
#  "l*t": ["lot"],
#  "lo*": ["lot", "log"],
#  "l*g": ["log"],
#  "c*g": ["cog"],
#  "co*": ["cog"]
#}

# word = "hit", path = ["hit"]
# queue = deque([("hot", ["hit", "hot"])])
# visited = {"hit"} 
# level_visited = {"hot"}

# queue = deque([("dot", ["hit", "hot", "dot"]),("lot", ["hit", "hot", "lot"])])
# visited = {"hit", "hot"}  # Updated after finishing the level
# level_visited = {"dot", "lot"}

# queue = deque([("dog", ["hit", "hot", "dot", "dog"]), ("log", ["hit", "hot", "lot", "log"])])
# visited = {"hit", "hot",, "dot", "lot"}  # Updated after finishing the level
# level_visited = {"dog", "log"}

# queue = deque()
# result = [["hit", "hot", "dot", "dog", "cog"],["hit", "hot", "lot", "log", "cog"]]

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
result = sol.findLadders(beginWord, endWord, wordList)
print(f"result = {result}")

# Same
beginWord = "hit"
endWord = "hit"
wordList = ["hot","dot","dog","lot","hit"]
result = sol.findLadders(beginWord, endWord, wordList)
print(f"result = {result}")

# no matching word, with one letter difference.
beginWord = "hit"
endWord = "xyz"
wordList = ["hot","dot","dog","lot","hit"]
result = sol.findLadders(beginWord, endWord, wordList)
print(f"result = {result}")
