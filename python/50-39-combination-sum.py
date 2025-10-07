class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                # you are appending a snapshot (a new list with the same values) at that moment
                # so even if cur changes later in recursion, the version already added to res stays intact
                # appends a SNAPSHOT
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # include candidates[i]
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()

            # skip candidates[i]
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res