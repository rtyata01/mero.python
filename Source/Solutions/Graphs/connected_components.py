
# find the connected components, given a list of connected edges and total number of nodes.
# Need bidirectional edges for your connected components algorithm i.e. u → v, and from v → u.
# DFS/BFS wouldn't find all nodes that are truly reachable in an undirected (Directed) graph, u → v but not  v → u.

from collections import defaultdict
class Solution:
    def numComponents(self, nodes: int, edges: list) -> int:
        # Create an adjacency list
        adj = defaultdict(list) # {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * nodes
        
        def dfs(node):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        components = 0
        for i in range(nodes):
            if not visited[i]:
                dfs(i)
                components += 1
        
        return components
    
# O(n)        → create node entries
# + O(e)      → build adjacency list
# + O(n)      → visited list
# + O(n + e)  → DFS traversal
#------------------------
# = O(n + e)

# Example Usage
sol = Solution()

n = 5 # note, node start from index 0 here but not index 1.
edges = [[0, 1], [1, 2], [3, 4]]
print(f"Number of connected components: {sol.numComponents(n, edges)}")
# The graph has 5 nodes and 2 connected components.
# Component 1 contains nodes 0, 1, 2 which are all connected.
# Component 2 contains nodes 3, 4, which are connected.

n = 7
edges = [[0, 1], [1, 2], [1, 3], [3, 4], [5, 6]]
print(f"Number of connected components: {sol.numComponents(n, edges)}")
# The graph has 7 nodes and 2 connected components.
# Component 1 contains nodes 0, 1, 2, 3, 4, which are all connected.
# Component 2 contains nodes 5, 6, which are connected.
