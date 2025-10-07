class Solution:
    # O (n* 4^n)
    # For those who wondered why there's no append or pop (similar to the other backtracking approaches) it's because strings are immutable. Everytime the call is made to the backtrack method, python creates a new string so when the method returns up the stack, the caller still has the original string without the concatenated letter.


    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digitToChar = {
            "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        res: List[str] = []

        def backtrack(i: int, cur: str) -> None:
            if i == len(digits):
                res.append(cur)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, cur + c)

        backtrack(0, "")
        return res