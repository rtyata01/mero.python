# Problem: Can all courses be finished given prerequisites?
# DFS → faster, cleaner, great for moderate graphs.
# BFS (Kahn) → safer for very deep graphs (no recursion limit issues), easier to reason about in iterative style.

from collections import defaultdict

def can_finish(num_courses, prerequisites):
    graph = defaultdict(list)  # [[] for _ in range(num_courses)]
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course) # prerequisite -> course
    
    visited = [0] * num_courses  # 0=unvisited, 1=visiting, 2=visited

    def dfs(node):
        if visited[node] == 1: # Cycle detected
            return False
        if visited[node] == 2: # Already processed
            return True
        
        visited[node] = 1 # Mark Visiting
        for nei in graph[node]:
            if not dfs(nei):
                return False
            
        visited[node] = 2 # Mark Visisted
        return True

    for i in range(num_courses):
        if visited[i] == 0 and not dfs(i):
            return False
    return True

# Time and Space Complexity: O(num_courses + len(prerequisites))
# Creating adj graph: O(num_courses)
# Adding edges: O(len(prerequisites))
# DFS traversal cost: O(num_courses + len(prerequisites))

from collections import deque

def can_finish_bfs(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque([i for i in range(num_courses) if indegree[i] == 0])
    visited = 0

    while queue:
        node = queue.popleft()
        visited += 1
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)

    return visited == num_courses


test_cases = [
    (2, []), # No prerequisites
    (2, [[1, 0]]), # Simple linear dependency
    (2, [[1, 0], [0, 1]]), # Simple cycle
    (4, [[1, 0], [2, 1], [3, 2]]), # Chain of dependencies
    (4, [[1, 0], [2, 1], [0, 2]]), # Cycle in dependencies
    (5, [[1, 0], [3, 2]]), # Disconnected graph with no cycle
    (5, [[1, 0], [3, 2], [2, 3]]) # Disconnected graph with a cycle
]

for test_case in test_cases:
    num_course, prerequisites = test_case
    print("DFS Output:", can_finish(num_course, prerequisites))
    print("BFS Output:", can_finish_bfs(num_course, prerequisites))
