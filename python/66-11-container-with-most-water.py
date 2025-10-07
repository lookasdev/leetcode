class Solution:
    def maxArea(self, height: List[int]) -> int:
        # # BRUTE FORCE (O(n^2)) — for reference:
        # res = 0
        # n = len(height)
        # for l in range(n):
        #     for r in range(l + 1, n):
        #         area = (r - l) * min(height[l], height[r])
        #         res = max(res, area)
        # return res

        # TWO-POINTER (O(n), O(1) space)
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            # width * limiting height
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            # Move the pointer at the shorter line to try to find a taller one
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res