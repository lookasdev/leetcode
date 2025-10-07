class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # 1) Find the first index i from the right such that nums[i] < nums[i+1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # 2) Find the rightmost index j > i with nums[j] > nums[i]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # 3) Swap pivot nums[i] with successor nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # 4) Reverse the suffix starting at i+1 (makes it the smallest order)
        # nums[i + 1:] = reversed(nums[i + 1:])
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        # Next Permutation Algorithm:
        # 1. Find pivot: scan from right, first i where nums[i] < nums[i+1].
        #    (Everything to the right is descending = largest order for that suffix.)
        #
        # 2. If no pivot found (array is fully descending),
        #    reverse whole array → it’s the last permutation, so wrap to first.
        #
        # 3. Otherwise, find successor: rightmost element > nums[i] in the suffix.
        #    Swap with nums[i] → makes the prefix just slightly larger.
        #    (so we don't jump to more than just the next permutation)
        #
        # 4. Reverse the suffix (i+1 .. end) to make it ascending,
        #    giving the smallest possible order for the new suffix.
        #
        # Result = the next lexicographic permutation.
        # Prefix: the part of the array before index i.
        # Suffix: the part of the array after index i.