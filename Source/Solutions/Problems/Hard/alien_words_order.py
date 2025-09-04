# Hard: Given sorted list of words in alien dictionary, find the correct character order in that language.

from collections import defaultdict, deque

def alien_order(words):
    # Step 1: Initialize graph
    graph = defaultdict(set) 
    in_degree = {char: 0 for word in words for char in word} # outer loop # followed by inner loop
    # {'w': 0, 'r': 0, 't': 0, 'f': 0, 'e': 0 }

    # Step 2: Build graph by comparing adjacent words
    for i in range(len(words) - 1):
        c_word, n_word = words[i], words[i+1]
        min_len = min(len(c_word), len(n_word))
        
        # Check for invalid ordering like ["abc", "ab"], where ab is expected to be first.
        if len(c_word) > len(n_word) and c_word[:min_len] == n_word[:min_len]:
            return "invalid order detected in inputs."

        for j in range(min_len):
            if c_word[j] != n_word[j]:
                if n_word[j] not in graph[c_word[j]]:
                    graph[c_word[j]].add(n_word[j])  # graph = {'t': {'f'}, 'w': {'e'},'r': {'t'},'e': {'r'}}
                    in_degree[n_word[j]] += 1       # in_degree = {'w': 0, 'r': 1, 't': 1, 'f': 1, 'e': 1} f depends on t, so degree 1.
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
        return "cannot find the error, cycle exists or gap exists"

    return "".join(order)


# Time Complexity =	O(n + u + p)
    # in_degree = O(n), where u is unique chars.
    # graph = O(n), where n is total words.
    # bfs = O(u + p), where p is number of precedence i.e. char dependencies.
    
# Space Complexity = O(u + p)
    # in_degree = O(u), where u is unique chars.
    # graph = O(u + p)
    # queue, order =  o(u)


words = ["x", "wrt", "wrf", "er", "ett", "rftt"]  # sorted list of words
print(alien_order(words))  # Output: "xwertf"

# in_degree = {'w': 0, 'r': 0, 't': 0, 'f': 0, 'e': 0 }
# graph = {'t': {'f'}, 'w': {'e'},'r': {'t'},'e': {'r'}}
# in_degree = {'w': 0, 'r': 1, 't': 1, 'f': 1, 'e': 1} , w has no dependency, so starting point. f depends on t, so degree 1.
# Use BFS for finding the order W -> e -> r -> t -> f

graph = defaultdict(set)
graph['a'].add('b')  # Works even if 'a' is not in graph yet

#graph = {}
#graph['a'].add('b')  # ERROR if 'a' not already in graph