# Problem: Given an n x n matrix where each row and column is sorted in ascending order, find the kth smallest element.
# Use a min-heap to track the smallest elements, starting from the top-left corner and exploring neighbors.
import heapq

def kthSmallest(matrix: list[list[int]], k: int) -> int:
    if not matrix:
        return
    
    n = len(matrix)
    heap = [(matrix[0][0], 0, 0)]
    seen = {(0, 0)}
    directions = [(0, 1), (1, 0)]  # Right and down
    
    for _ in range(k - 1):
        val, row, col = heapq.heappop(heap)
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if new_row < n and new_col < n and (new_row, new_col) not in seen:
                heapq.heappush(heap, (matrix[new_row][new_col], new_row, new_col))
                seen.add((new_row, new_col))
                
    return heap[0][0]

# Time Complexity: O(k log k)
# Space Complexity: O(k)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f" 1st smallest element is: {kthSmallest(matrix, 1)}")
print(f" 6th smallest element is: {kthSmallest(matrix, 6)}")
print(f" 9th smallest element is: {kthSmallest(matrix, 9)}")