class Solution:
    # O(n * m * dfs) # dfs is 4^len(word) # 4 because we check in every direction: up, down, left, right
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()  # cells in current path (visited)

        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                board[r][c] != word[i] or (r, c) in path):
                return False

            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c)) # if not removed from path, that cell would stay "blocked" forever for other search paths
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False