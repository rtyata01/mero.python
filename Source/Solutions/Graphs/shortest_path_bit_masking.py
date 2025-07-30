# Compute the length of the shortest path that visits every node in a graph at least once, using Breadth-First Search (BFS) with bitmasking.
# Shortest Path Visiting All Nodes problem — similar to a Traveling Salesperson Problem.

from collections import deque

def shortest_path_length(nodes, edges):
    graph = {i: [] for i in range(nodes)}
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    all_visited = (1 << nodes) - 1  # Bitmask when all nodes are visited 1 << 4 = 0b10000 - 1 = 0b01111 where n = 4
    queue = deque()
    visited = set()

    # Initialize BFS with each node as a starting point
    for node in range(nodes):
        mask = 1 << node  # left shift 1 by node value i.e. 0, 1, 2 and 3.
        queue.append((node, mask, 0))  # (current_node, visited_mask, steps)
        visited.add((node, mask))

    while queue:
        current_node, visited_mask, steps = queue.popleft()

        # If all nodes are visited, return the number of steps
        if visited_mask == all_visited:
            return steps

        for neighbor in graph[current_node]:
            next_mask = visited_mask | (1 << neighbor)
            state = (neighbor, next_mask)
            if state not in visited:
                visited.add(state)
                queue.append((neighbor, next_mask, steps + 1))

    return -1  # If no valid path exists (shouldn't happen for connected graphs)

# Time Complexity: O (n 2^n),
    # With BFS, Each node can be visited with 2^n distinct states i.e. visited mask.
# Space Complexity:  O (n 2^n)
    # Stores up to n × 2^n state combinations.
    # worst case, all n × 2^n states can be queued.

# Example usage
nodes = 5
edges = [[0, 1], [1, 2], [1, 3], [3, 4]]

# 0 — 1 — 2
#     |
#     3 — 4

# 0 -> 1 -> 2 -> 1 -> 3 -> 4
print(f"Expected: 5, Shortest Path Length: {shortest_path_length(nodes, edges)}")

nodes = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]
# 0 — 1 — 2
#   \     |
#     4 — 3
# 0 -> 1 -> 2 -> 3 -> 4
print(f"Expected: 4, Shortest Path Length: {shortest_path_length(nodes, edges)}")

nodes = 7
edges = [[0, 1], [1, 2], [1, 3], [3, 4], [5, 6]]
print(f"Expected: -1, Shortest Path Length: {shortest_path_length(nodes, edges)}")
