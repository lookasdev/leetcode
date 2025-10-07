class Solution:
    # iterative
    # O(n! * n^2) time complexity
    # O(n! * n) space complexity
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)
            perms = new_perms

        return perms

    # recursive
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     # base case
    #     if len(nums) == 0:
    #         return [[]]

    #     perms = self.permute(nums[1:])  # permutations of the rest
    #     res = []

    #     for p in perms:
    #         for i in range(len(p) + 1):  # insert nums[0] at every position
    #             p_copy = p.copy()
    #             p_copy.insert(i, nums[0])
    #             res.append(p_copy)

    #     return res

    # recursive backtracking
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     result = []

    #     # base case
    #     if len(nums) == 1:
    #         return [nums.copy()] # return [nums[:]]

    #     for i in range(len(nums)):
    #         n = nums.pop(0)                # take first element out
    #         perms = self.permute(nums)     # get all perms of remaining nums

    #         for perm in perms:
    #             perm.append(n)             # add the removed number back

    #         result.extend(perms)
    #         nums.append(n)                 # put number back for the next iteration

    #     return result
