def find_longest_increasing_path(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    directions = [(-1 , 0), (1 , 0), (0, -1), (0, 1)] # up, down, left, right

    def dfs(x, y, visited):
        max_length = 1
        min_path_sum = grid[x][y]
        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited) and grid[nx][ny] > grid[x][y]: # for decreasing use <
                length, path_sum = dfs(nx, ny, visited)
                length += 1
                path_sum += grid[x][y]

                if length > max_length:
                    max_length = length
                    min_path_sum = path_sum
                elif length == max_length:
                    min_path_sum = min(min_path_sum, path_sum)

        visited.remove((x, y))  # Backtrack
        return max_length, min_path_sum

    longest = 0
    min_sum = float('inf')
    for i in range(rows):
        for j in range(cols):
            length, path_sum = dfs(i, j, set())
            if length > longest:
                longest = length
                min_sum = path_sum
            elif length == longest:
                min_sum = min(min_sum, path_sum)
    return min_sum

grid = [
    [9,  9, 4],
    [6, -1, 8],
    [2,  1, 1]
]
print(f"Expected: 17, Longest strictly increasing path sum: {find_longest_increasing_path(grid)}")  # -1 -> 1 -> 2 -> 6 -> 9

grid = [
    [9, 9, 4],
    [3, 4, 5],
    [2, 1, 1]
]
print(f"Expected: 15, Longest strictly increasing path sum:: {find_longest_increasing_path(grid)}") # 1 -> 2 -> 3 -> 4 -> 5