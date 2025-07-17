from collections import defaultdict, deque

def findLadders(beginWord, endWord, wordList):
    if beginWord == endWord:
        return [[beginWord]]
        
    wordSet = set(wordList)
    if endWord not in wordSet:
        return []

    # Step 1: BFS to build the graph of shortest paths
    layer = {}
    layer[beginWord] = [[beginWord]]

    while layer:
        new_layer = defaultdict(list)
        for word in layer:
            if word == endWord:
                return layer[word]  # All sequences reaching endWord at shortest length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wordSet:
                        new_layer[new_word] += [path + [new_word] for path in layer[word]]
        wordSet -= set(new_layer.keys())
        layer = new_layer

    return []

# Time Complexity:
# Total: O(N × L × 26 + P × N) , where N = words, L is lenght of each word, BFS path propagation is P * N.

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
result = findLadders(beginWord, endWord, wordList)
print(f"result = {result}")

# step 1
# new_layer["hot"] += [["hit", "hot"]]
# wordSet = {"dot", "dog", "lot", "log", "cog"}
# layer = { "hot": [["hit", "hot"]]}

# step 2
# new_layer["dot"] += [path + ["dot"] for path in layer["hot"]]
# new_layer["dot"] = [["hit", "hot", "dot"]]

# new_layer["lot"] += [path + ["lot"] for path in layer["hot"]]
# new_layer["lot"] = [["hit", "hot", "lot"]]
# wordSet = {"dog", "log", "cog"}
# layer = { "dot": [["hit", "hot", "dot"]], "lot": [["hit", "hot", "lot"]]}

# step 3
# new_layer["dog"] = [["hit", "hot", "dot", "dog"]]
# new_layer["log"] = [["hit", "hot", "lot", "log"]]
# wordSet = {"cog"}
# layer = { "dog": [["hit", "hot", "dot", "dog"]], "log": [["hit", "hot", "lot", "log"]]}

# step 4
# new_layer["cog"] += [path + ["cog"] for path in layer["dog"]]
# new_layer["cog"] += [path + ["cog"] for path in layer["log"]]
# layer = { "cog": [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]}


# endWord not in list.
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
result = findLadders(beginWord, endWord, wordList)
print(f"result = {result}")

# Same
beginWord = "hit"
endWord = "hit"
wordList = ["hot","dot","dog","lot","hit"]
result = findLadders(beginWord, endWord, wordList)
print(f"result = {result}")

# no matching word, with one letter difference.
beginWord = "hit"
endWord = "xyz"
wordList = ["hot","dot","dog","lot","hit"]
result = findLadders(beginWord, endWord, wordList)
print(f"result = {result}")


