class Solution:
    # time complexity: O(n * sum(nums))
    # space complexity similar but improved with dp instead of dfs with cache (backtracking) -> O(sum(nums))
    def canPartition(self, nums: List[int]) -> bool:
        # total sum must be even to split equally
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2
        dp = {0}  # set of reachable sums

        for i in range(len(nums) - 1, -1, -1):
            next_dp = set()
            for t in dp:
                if t + nums[i] == target:
                    return True  # early exit if we hit target
                next_dp.add(t + nums[i])  # take nums[i]
                next_dp.add(t)            # skip nums[i]
            dp = next_dp

        return target in dp