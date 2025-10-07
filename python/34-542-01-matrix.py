class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        q = deque()
        res = [[-1] * COLS for _ in range(ROWS)]  # -1 = unvisited

        # Enqueue all zero cells (water cells in leetcode 1765)
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0: # if mat[r][c]:
                    q.append((r, c))
                    res[r][c] = 0

        # BFS
        while q:
            r, c = q.popleft()
            h = res[r][c]
            neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]

            for nr, nc in neighbors:
                if nr < 0 or nc < 0 or nr == ROWS or nc == COLS:
                    continue
                if res[nr][nc] != -1: # means element already visited since default value was changed
                    continue
                res[nr][nc] = h + 1
                q.append((nr, nc))

        return res