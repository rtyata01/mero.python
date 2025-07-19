# Problem: Can all courses be finished given prerequisites?

def can_finish(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    for course, prerequisite in prerequisites:
        graph[course].append(prerequisite)
    
    visited = [0] * num_courses  # 0=unvisited, 1=visiting, 2=visited

    def dfs(node):
        if visited[node] == 1:
            return False
        if visited[node] == 2:
            return True
        
        visited[node] = 1
        for nei in graph[node]:
            if not dfs(nei):
                return False
        visited[node] = 2
        return True

    return all(dfs(i) for i in range(num_courses))

# Time and Space Complexity: O(num_courses + len(prerequisites))
# Creating adj graph: O(num_courses)
# Adding edges: O(len(prerequisites))
# DFS traversal cost: O(num_courses + len(prerequisites))

# Test 1 - No prerequisites
print("Expected: True,", "Output:", can_finish(2, []))

# Test 2 - Simple linear dependency
print("Expected: True,", "Output:", can_finish(2, [[1, 0]]))

# Test 3 - Simple cycle
print("Expected: False,", "Output:", can_finish(2, [[1, 0], [0, 1]]))

# Test 4 - Chain of dependencies
print("Expected: True,", "Output:", can_finish(4, [[1, 0], [2, 1], [3, 2]]))

# Test 5 - Cycle in dependencies
print("Expected: False,", "Output:", can_finish(4, [[1, 0], [2, 1], [0, 2]]))

# Test 6 - Disconnected graph with no cycle
print("Expected: True,", "Output:", can_finish(5, [[1, 0], [3, 2]]))

# Test 7 - Disconnected graph with a cycle
print("Expected: False,", "Output:", can_finish(5, [[1, 0], [3, 2], [2, 3]]))