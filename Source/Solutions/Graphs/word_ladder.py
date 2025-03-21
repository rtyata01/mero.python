from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list) -> list:
        if endWord not in wordList:
            return []
        
        wordList = set(wordList)
        # Create an adjacency list where each word is linked to wordsm, with one letter or character different
        adj_list = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]  # For example, word hit have pattern h*t, hi*, *it
                adj_list[pattern].append(word)
        
        # BFS to find the shortest paths
        queue = deque([(beginWord, [beginWord])])
        visited = set()
        visited.add(beginWord)
        found = False
        result = []
        
        while queue and not found:
            level_visited = set()
            for _ in range(len(queue)):
                word, path = queue.popleft()
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    for neighbor in adj_list[pattern]:
                        if neighbor == endWord:
                            result.append(path + [endWord])
                            found = True
                        if neighbor not in visited:
                            level_visited.add(neighbor)
                            queue.append((neighbor, path + [neighbor]))
            visited.update(level_visited)
        
        return result

# Example Usage
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

sol = Solution()
print(f"All shortest transformation sequences: {sol.findLadders(beginWord, endWord, wordList)}")
