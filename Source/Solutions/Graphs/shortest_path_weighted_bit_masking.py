# Compute the length of the weighted shortest path that visits every node in a graph at least once, using Breadth-First Search (BFS) with bitmasking.
# Shortest Path Visiting All Nodes problem — similar to a Traveling Salesperson Problem.

from collections import deque
import heapq

def find_weighted_shortest_path(nodes, edges):
    graph = {i: [] for i in range(nodes)}
    
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    all_visited = (1 << nodes) - 1
    min_heap = []
    visited = set()

    # Initialize with each node as starting point, cost=0
    for node in range(nodes):
        mask = 1 << node
        heapq.heappush(min_heap, (0, node, mask))  # (cost, node, visited_mask) # use negative for (max_heap, (-0, node, mask))
        visited.add((node, mask))

    while min_heap:
        cost, node, mask = heapq.heappop(min_heap)

        if mask == all_visited:
            return cost

        for neighbor, weight in graph[node]:
            next_mask = mask | (1 << neighbor)
            state = (neighbor, next_mask)
            next_cost = cost + weight
            if state not in visited:
                visited.add(state)
                heapq.heappush(min_heap, (next_cost, neighbor, next_mask))  # use negative for (max_heap, (-next_cost, neighbor, next_mask))

    return -1


# Time Complexity: O (n 2^n),
    # With BFS, Each node can be visited with 2^n distinct states i.e. visited mask.
# Space Complexity:  O (n 2^n)
    # Stores up to n × 2^n state combinations.
    # worst case, all n × 2^n states can be queued.

# Example usage
nodes = 4
edges = [
    (0, 1, 2),  # edge from node 0 to 1 with weight 2
    (0, 2, 5),  # edge from node 0 to 2 with weight 5
    (1, 2, 1),  # edge from node 1 to 2 with weight 1
    (1, 3, 4),  # edge from node 1 to 3 with weight 4
    (2, 3, 1),  # edge from node 2 to 3 with weight 1
]
# 0 -> 1 -> 2 -> 3 = 2 + 1 + 1 = 4
# 0 -> 1 -> 3 -> 2 = 2 + 4 + 1 = 7
# 1 -> 0 -> 2 -> 3 = 2 + 5 + 1 = 8
print(f"Expected: 4, Shortest Path Length: {find_weighted_shortest_path(nodes, edges)}")

nodes = 6
edges = [
    (0, 1, 3), # edge from node 0 to 1 with weight 3
    (1, 2, 4), # edge from node 1 to 2 with weight 4
    (3, 4, 2), # edge from node 3 to 4 with weight 2
    (4, 5, 1)  # edge from node 4 to 5 with weight 1
]
# missing connection from node 2 to node 3.
print(f"Expected: -1, Shortest Path Length: {find_weighted_shortest_path(nodes, edges)}")

