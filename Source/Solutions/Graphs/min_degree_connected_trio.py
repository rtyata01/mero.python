# Find the minimum degree among all connected trios in the graph.
# If no connected trio exists, return -1.

# degree_of_trio= (deg(u) + deg(v) + deg(w)) −2 × (number of edges between u, v, w)

import math

def min_trio_degree(n, edges):
    # Build adjacency matrix for fast edge lookup
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    
    # Track node degrees
    degree = [0] * (n + 1)

    for u, v in edges:
        graph[u][v] = True
        graph[v][u] = True
        degree[u] += 1
        degree[v] += 1

    min_trio = math.inf

    # Try all triplets (i, j, k)
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if not graph[i][j]:   # equivalent to (graph[i][j] == False)
                continue
            for k in range(j + 1, n + 1):
                if graph[i][k] and graph[j][k]:  # equivalent to (graph[i][k] == True)
                    # Connected trio found
                    # Trio degree = sum of degrees - 6
                    total_deg = degree[i] + degree[j] + degree[k] - 6
                    min_trio = min(min_trio, total_deg)

    return min_trio if min_trio != math.inf else -1


n = 6
edges = [[1, 2], [2, 3], [3, 1], [4, 1], [5, 2], [6, 3]]
print(f"Expected: 3, Expected Min Tri Degree: ", min_trio_degree(n, edges))  # Output: 0


#     4
#   /
# 1 ----2 ----5
#  \   /
#    3
#    |
#    6
# 
# d(1), d(2), d(3) = 3 connected nodes
# d(4), d(5), d(6) = 1 connected node
# min_trio = 9 - 2 * (number of internal edges) = 9-2 * 3 = 9-6 = 3

# if you add connections from 1 to 6, then 1, 3 and 6 will be another connected trio.
# min_trio(1,3,6) = 4 + 3 + 2 - 6 = 3
# min_trio(1,2,3) = 4 + 3 + 3 - 6 = 4
n = 6
edges = [[1, 2], [1, 6], [2, 3], [3, 1], [4, 1], [5, 2], [6, 3]]
print(f"Expected: 3, Expected Min Tri Degree: ", min_trio_degree(n, edges))  # Output: 0