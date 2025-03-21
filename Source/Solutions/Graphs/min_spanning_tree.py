import heapq

class Solution:
    def minSpanningTree(self, n: int, edges: list) -> int:
        """ A Minimum Spanning Tree is a subset of the edges of a graph that connects all the vertices together, without any cycles, and with the minimum possible total edge weight."""
        
        adj = {i: [] for i in range(n)}
        for u, v, weight in edges:
            adj[u].append((v, weight))
            adj[v].append((u, weight))
        
        # Prim's algorithm
        min_heap = [(0, 0)]  # (weight, node) The heap will need to prioritize the weight first, so order matters.
        in_mst = [False] * n
        mst_weight = 0
        edges_used = 0
        
        while min_heap and edges_used < n:
            weight, node = heapq.heappop(min_heap)
            if in_mst[node]:
                continue
            in_mst[node] = True
            mst_weight += weight
            edges_used += 1
            
            for neighbor, edge_weight in adj[node]:
                if not in_mst[neighbor]:
                    heapq.heappush(min_heap, (edge_weight, neighbor))
        
        return mst_weight

# Example Usage
sol = Solution()
n = 4
edges = [[0, 1, 1], [0, 2, 2], [1, 2, 3], [1, 3, 1], [2, 3, 1]]
print(f"Minimum spanning tree weight: {sol.minSpanningTree(n, edges)}")
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
print(f"Minimum spanning tree weight: {sol.minSpanningTree(n, edges)}")
# The smallest edges are selected to grow the MST: (0, 2), (1, 2), (1, 3), (3, 4) and (3, 5)
# The total weight of the MST is: 3 + 1 + 2 + 2 + 3 = 11.