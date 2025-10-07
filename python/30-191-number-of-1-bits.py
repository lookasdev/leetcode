class Solution:
    # def hammingWeight(self, n: int) -> int:
        # res = 0
        # while n:
        #     res += n % 2   # add 1 if the last bit is set
        #     n = n >> 1     # shift right by 1 (removes last bit)
        # return res

    # check for 1's only
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n - 1)   # removes the lowest set bit
            res += 1
        return res