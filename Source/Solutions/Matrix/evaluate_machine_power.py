# Given n rows (machines) with m elements (power units). 
    # Each row can transfer at most one element (the smallest).
    # Find maximum sum of the minimal across rows after transfer.
# For small n (≤ 32), use the DFS + memoization solution we already implemented.
# For large n (≈ 10^5), DFS solution is not feasible. Use Dynamic programming solution to avoid recusion stack overflow for large n.

from functools import lru_cache

def max_sum_of_min(matrix):
    n = len(matrix)
    if n == 0:
        return 0

    # Convert to tuples for immutability
    init_state = tuple(tuple(row) for row in matrix)

    @lru_cache(maxsize=None)
    def dfs(i, state):
        if i == n:  # processed all rows
            return sum(min(r) for r in state if r)

        max_power = dfs(i+1, state)  # option: no transfer

        rows = [list(r) for r in state]

        # Only try transferring the **minimum** element of row i
        if rows[i]:  # row not empty
            # find min without sorting
            min_val = min(rows[i])
            min_index = rows[i].index(min_val)

            # Transfer to previous row if possible
            if i - 1 >= 0:
                new_rows = [r.copy() for r in rows]
                new_rows[i].pop(min_index)
                new_rows[i-1].append(min_val)
                new_state = tuple(tuple(r) for r in new_rows)
                max_power = max(max_power, dfs(i+1, new_state))

            # Transfer to next row if possible
            if i + 1 < n:
                new_rows = [r.copy() for r in rows]
                new_rows[i].pop(min_index)
                new_rows[i+1].append(min_val)
                new_state = tuple(tuple(r) for r in new_rows)
                max_power = max(max_power, dfs(i+1, new_state))

        return max_power

    return dfs(0, init_state)

# Test
print(max_sum_of_min([[1,5],[4,3],[2,10]]))          # 16
print(max_sum_of_min([[2,7,4],[2,4,3]]))             # 6
print(max_sum_of_min([[2,2,2,2],[2,4,3,2],[2,5,3,3]])) # 7
print(max_sum_of_min([[2],[3]]))                     # 5