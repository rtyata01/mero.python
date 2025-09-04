# A Minimum Spanning Tree is, refers minimal weight visiting all nodes. 
# A subset of the edges of a graph that connects all the vertices/nodes together, 
    # without any cycles, 
    # With the minimum possible total edge weight.

import heapq
from collections import defaultdict

class Solution:
    def min_spanning_tree_weight(self, nodes: int, edges: list) -> int:
        if nodes == 0:
            return 0
        
        # Build adjacency list
        adj = defaultdict(list) # {i: [] for i in range(n)}
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        visited = [False] * nodes
        min_heap = [(0, 0)]  # Start with edge weight 0, from node 0.
        total_weight = 0
        nodes_visited = 0
        
        while min_heap and nodes_visited < nodes:
            weight, node = heapq.heappop(min_heap)
            if visited[node]:
                continue
            
            visited[node] = True
            total_weight += weight
            nodes_visited += 1
            
            for neighbor, w in adj[node]:
                if not visited[neighbor]:
                    heapq.heappush(min_heap, (w, neighbor))
        
        # Check if all nodes were visited (i.e., graph is connected)
        return total_weight if nodes_visited == nodes else -1

# Time Complexity
# Building Graph = o(e) = e is number of edges, n is number of nodes
# Heap operations: o(e log n) = heap insertions for each edge e with o(log n)

# Example Usage
sol = Solution()
n = 4
edges = [[0, 1, 1], [0, 2, 2], [1, 2, 3], [1, 3, 1], [2, 3, 1]] # edges with weight
print(f"Minimum spanning tree weight: {sol.min_spanning_tree_weight(n, edges)}")
#  (0) --1-- (1)
#   |      /   |
#  2|   3/    1|
#   |  /       |
#  (2) --1-- (3)
# The smallest edges are selected to grow the MST: (0, 1), (1, 3), and (2, 3).
# The total weight of the MST will be the sum of these edges: 1 + 1 + 1 = 3.

n = 6
edges = [
    [0, 1, 4],  # Edge between node 0 and node 1 with weight 4
    [0, 2, 3],  # Edge between node 0 and node 2 with weight 3
    [1, 2, 1],  # Edge between node 1 and node 2 with weight 1
    [1, 3, 2],  # Edge between node 1 and node 3 with weight 2
    [2, 3, 4],  # Edge between node 2 and node 3 with weight 4
    [3, 4, 2],  # Edge between node 3 and node 4 with weight 2
    [4, 5, 6],  # Edge between node 4 and node 5 with weight 6
    [3, 5, 3],  # Edge between node 3 and node 5 with weight 3
    [0, 5, 7]   # Edge between node 0 and node 5 with weight 7
]
print(f"Minimum spanning tree weight: {sol.min_spanning_tree_weight(n, edges)}")
# The smallest edges are selected to grow the MST: (0, 2), (1, 2), (1, 3), (3, 4) and (3, 5)
# The total weight of the MST is: 3 + 1 + 2 + 2 + 3 = 11.