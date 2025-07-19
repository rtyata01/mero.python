# Hard: Given a list of courses and their prerequisites, return the order in which to take the courses. If impossible, return an empty array.

from collections import defaultdict, deque

def find_course_order(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * numCourses
    
    # Build graph
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
    
    # Initialize queue with courses having no prerequisites
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    order = []
    
    while queue:
        course = queue.popleft()
        order.append(course)
        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)
    
    return order if len(order) == numCourses else []

# Time Complexity: o(C + P), where C is number of courses and P is number of prerequisites.
# Space Complexity: o(C + P)

# Example usage:
numCourses = 4
prerequisites = [[1,0], [2,0], [3,1], [3,2]]  # (course, prerequisite)
print(f"Expected: [0,1,2,3] : Computed course order: ", find_course_order(numCourses, prerequisites)) 

numCourses = 2
prerequisites = []  # (no prerequisite)
print(f"Expected: [0,1] : Computed course order: ", find_course_order(numCourses, prerequisites)) 

numCourses = 2
prerequisites = [[0,1],[1,0]]  # (cyclic prerequisite)
print(f"Expected: [] : Computed course order: ", find_course_order(numCourses, prerequisites)) 
