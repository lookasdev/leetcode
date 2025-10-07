class Solution:
    # T: O(n * 2^n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        subset: List[int] = []

        def dfs(i: int) -> None:
            if i == len(nums):
                res.append(subset.copy())
                return
            # include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # exclude nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res