class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0      # rob1 = best up to i-2, rob2 = best up to i-1
        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)  # take this house (n+rob1) or skip (rob2)
            rob1 = rob2                 # shift window: new i-2 becomes old i-1
            rob2 = temp                 # new i-1 becomes dp[i]
        return rob2
