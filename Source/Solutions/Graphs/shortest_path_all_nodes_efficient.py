# Compute the shortest path length that visits every node in an undirected, connected graph at least once. 
# Shortest Path Visiting All Nodes problem — similar to a Traveling Salesperson Problem.

from collections import deque

def shortest_path_length(graph):
    n = len(graph)
    all_visited = (1 << n) - 1  # Bitmask when all nodes are visited
    queue = deque()
    visited = set()

    # Initialize BFS with each node as a starting point
    for node in range(n):
        mask = 1 << node
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

# Example usage
graph = [
    [1, 2, 3],  # Node 0 connects to 1, 2, 3
    [0],        # Node 1 connects to 0
    [0],        # Node 2 connects to 0
    [0]         # Node 3 connects to 0
]

print(f"Expected: 4, Shortest Path Length: {shortest_path_length(graph)}")

graph = [
    [1, 2],    # Node 0 connects to 1 and 2
    [0, 2, 3], # Node 1 connects to 0, 2, and 3
    [0, 1],    # Node 2 connects to 0 and 1
    [1]        # Node 3 connects to 1
]

print(f"Expected: 3, Shortest Path Length: {shortest_path_length(graph)}")
