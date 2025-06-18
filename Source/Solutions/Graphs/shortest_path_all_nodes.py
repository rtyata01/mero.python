from collections import deque

def shortestPathLength(graph):
    n = len(graph)
    final_state = (1 << n) - 1  # All nodes visited
    queue = deque()
    visited = set()

    # Initialize: start from each node
    for i in range(n):
        mask = 1 << i
        queue.append((i, mask, 0))  # (node, visited_mask, steps)
        visited.add((i, mask))

    while queue:
        node, mask, steps = queue.popleft()
        
        if mask == final_state:
            return steps

        for neighbor in graph[node]:
            next_mask = mask | (1 << neighbor)
            state = (neighbor, next_mask)
            if state not in visited:
                visited.add(state)
                queue.append((neighbor, next_mask, steps + 1))

    return -1  # Not possible

graph = [
    [1, 2, 3],  # Node 0 connects to 1, 2, 3
    [0],        # Node 1 connects to 0
    [0],        # Node 2 connects to 0
    [0]         # Node 3 connects to 0
]

print(f"Expected:4, Shortest Path Length:", shortestPathLength(graph)) 

graph = [
    [1, 2],    # Node 0 connects to 1 and 2
    [0, 2, 3], # Node 1 connects to 0, 2, and 3
    [0, 1],    # Node 2 connects to 0 and 1
    [1]        # Node 3 connects to 1
]

print(f"Expected:3, Shortest Path Length:", shortestPathLength(graph)) 
