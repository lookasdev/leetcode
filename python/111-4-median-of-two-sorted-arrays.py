class Solution:
    # O(log(min(n,m))) # because we run the binary search on the smaller array
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # ensure A is the smaller array
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2          # partition index in A
            j = half - i - 2          # partition index in B # -2 because both i and j start from 0
            # int partitionY = half - (partitionX + 1) - 1;  
            
			# PartitionX is 0 indexed so you need to add 1 to exactly know the size of partition 1.
            # Then you subtract it from half to know the size of partition B.
            # Once you do that  extra -1 at the end  because we want to calculate index of partitionY.
            # Partition should be 0 indexed as we are dealing with arrays.
            # Even if you calculate this, you get half - partitionX - 2 in the end.

            Aleft  = A[i]     if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft  = B[j]     if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            # correct partition
            # max of left side ≤ min of right side across both arrays.
            # So every element on the left partition is ≤ every element on the right partition—i.e., the cut is correct and you can read the median from the border elements.

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:  # odd
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            elif Aleft > Bright:
                r = i - 1
            elif Bleft > Aright:
            # else:
                l = i + 1

            # “Cut” = the partition point where we split both arrays into left and right parts.

            # Pick indices i (in A) and j (in B) so the left side has exactly half elements total (A[0..i] + B[0..j]), and the right side has the rest.

            # If max(left) ≤ min(right) (Aleft ≤ Bright and Bleft ≤ Aright), the cut is valid, and the median is at that boundary.