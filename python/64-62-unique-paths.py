class Solution:
    # T: O(m * n) # size of matrix, m are rows, n are columns
    # S: O(n) # length of a row
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n  # base case: last row has only 1 way

        for i in range(m - 1):  # iterate over rows from bottom to top
            newRow = [1] * n
            for j in range(n - 2, -1, -1):  # fill from right to left
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow

        return row[0]