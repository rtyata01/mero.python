from collections import defaultdict, deque

def alien_order(words):
    # Step 1: Initialize graph
    graph = defaultdict(set) 
    in_degree = {char: 0 for word in words for char in word} # outer loop # followed by inner loop
    # {'w': 0, 'r': 0, 't': 0, 'f': 0, 'e': 0 }


    # Step 2: Build graph by comparing adjacent words
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i+1]
        min_len = min(len(word1), len(word2))
        
        # Check for prefix case like ["abc", "ab"]
        if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
            return ""

        for j in range(min_len):
            if word1[j] != word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])  # graph = {'t': {'f'}, 'w': {'e'},'r': {'t'},'e': {'r'}}
                    in_degree[word2[j]] += 1       # in_degree = {'w': 0, 'r': 1, 't': 1, 'f': 1, 'e': 1} f depends on t, so degree 1.
                break

    # Step 3: Topological sort (BFS using queue)
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    order = []

    while queue:
        char = queue.popleft()
        order.append(char)

        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If not all characters are in the result → cycle exists
    if len(order) < len(in_degree):
        return ""

    return "".join(order)


words = ["wrt", "wrf", "er", "ett", "rftt"]
print(alien_order(words))  # Output: "wertf"

# in_degree = {'w': 0, 'r': 0, 't': 0, 'f': 0, 'e': 0 }
# graph = {'t': {'f'}, 'w': {'e'},'r': {'t'},'e': {'r'}}
# in_degree = {'w': 0, 'r': 1, 't': 1, 'f': 1, 'e': 1} , w has no dependency, so starting point. f depends on t, so degree 1.
# Use BFS for finding the order W -> e -> r -> t -> f

graph = defaultdict(set)
graph['a'].add('b')  # Works even if 'a' is not in graph yet

#graph = {}
#graph['a'].add('b')  # ERROR if 'a' not already in graph