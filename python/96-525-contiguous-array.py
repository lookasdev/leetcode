class Solution:
    # 111000
    # How to know to shrink window or increase?
    # Have to split, thus recursive and worse than O(n^2)

    # Not every result starts at beginning, e.g.
    # 11100

    # Is it possible to know exactly where 
    # the first 1 was, and verify that after it 
    # count[1] == count[0]?

    # Map each index to pair (count[0], count[1])
    # Use diff between counts for O(1) lookup of what we need

    def findMaxLength(self, nums: List[int]) -> int:
        zero, one = 0, 0
        res = 0

        diff_index = {}  # count[1] - count[0] -> earliest index

        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1

            if (one - zero) not in diff_index:
                diff_index[one - zero] = i

            if one == zero:
                res = one + zero
            else:
                idx = diff_index[one - zero]
                # diff(i) = diff(j)
                # ⇒ ones(i) − zeros(i) = ones(j) − zeros(j)
                # ⇒ (ones(i) − ones(j)) = (zeros(i) − zeros(j))
                res = max(res, i - idx)

        return res