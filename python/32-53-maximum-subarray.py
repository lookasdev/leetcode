class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)

        return maxSub

    # sol = Solution()
    # print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6 (subarray [4,-1,2,1])

    # version that also returns the actual subarray
    # def maxSubArray(self, nums: List[int]) -> Tuple[int, List[int]]:
    #     maxSub = nums[0]
    #     curSum = 0
    #     start = 0
    #     end = 0
    #     temp_start = 0

    #     for i, n in enumerate(nums):
    #         if curSum < 0:
    #             curSum = 0
    #             temp_start = i   # reset potential subarray start
    #         curSum += n

    #         if curSum > maxSub:
    #             maxSub = curSum
    #             start = temp_start
    #             end = i

    #     return maxSub, nums[start:end+1]