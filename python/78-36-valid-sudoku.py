class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)  # key = (r//3, c//3)


        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                if (val in rows[r]) or (val in cols[c]) or (val in boxes[(r//3, c//3)]):
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r//3, c//3)].add(val)
        return True

    # without using defaultdict(set)
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     rows, cols, boxes = {}, {}, {}  # maps: index/key -> set

    #     for r in range(9):
    #         for c in range(9):
    #             val = board[r][c]
    #             if val == '.':
    #                 continue

    #             if r not in rows:   rows[r] = set()
    #             if c not in cols:   cols[c] = set()
    #             b = (r//3, c//3)
    #             if b not in boxes:  boxes[b] = set()

    #             if (val in rows[r]) or (val in cols[c]) or (val in boxes[b]):
    #                 return False

    #             rows[r].add(val)
    #             cols[c].add(val)
    #             boxes[b].add(val)
    #     return True