class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue  # skip duplicates for the first number

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0: # because left pointer was modified at the bottom, right pointer will also adjust for the sum, thus avoiding duplicates for the third number as well
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # skip duplicates for the second number (left pointer modified here)
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res