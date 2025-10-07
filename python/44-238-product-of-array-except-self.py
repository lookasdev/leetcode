class Solution:
    # solution without separate prefix and postfix arrays
    # Time: O(n) (two linear passes)
    # Space: O(1) extra (besides output array)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

    # solution with separate prefix and postfix arrays
    # Space now is: O(n) extra
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     prefix = [1] * n
    #     postfix = [1] * n
    #     res = [1] * n

    #     # Build prefix products
    #     for i in range(1, n):
    #         prefix[i] = prefix[i - 1] * nums[i - 1]

    #     # Build postfix products
    #     for i in range(n - 2, -1, -1):
    #         postfix[i] = postfix[i + 1] * nums[i + 1]

    #     # Result = prefix[i] * postfix[i]
    #     for i in range(n):
    #         res[i] = prefix[i] * postfix[i]

    #     return res