class Solution:
	# T and S: O(m*n)
    def getFood(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = collections.deque()
        visited = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "*":
                    queue.append((row, col, 0))
                    visited.add((row, col))
                    break

        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        while queue:
            cur_row, cur_col, steps = queue.popleft()

            if grid[cur_row][cur_col] == "#":
                return steps
            else:
                for row_inc, col_inc in directions:
                    new_row = cur_row + row_inc
                    new_col = cur_col + col_inc

                    if (0 <= new_row < rows) and (0 <= new_col < cols) and grid[new_row][new_col] != "X":
                        if (new_row, new_col) not in visited:
                            visited.add((new_row, new_col))
                            queue.append((new_row, new_col, steps + 1))

        return -1

# Two important details:

# - **Mark visited on enqueue** (as your code does). This prevents the same cell from being enqueued multiple times at different distances.
    
# - This works because **every move costs 1**. If edges had different weights, you’d need a **priority queue (Dijkstra)**, not plain BFS.
  
# So: the queue isn’t sorted by `steps`; the **FIFO order + layer-by-layer discovery** makes pops come out in **nondecreasing distance**.

# nondecreasing meaning ascending with ties allowed