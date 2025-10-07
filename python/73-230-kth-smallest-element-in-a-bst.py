# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # an inorder traversal of a BST yields values in ascending order
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root

        while cur or stack:              # traverse until all nodes processed
            while cur:                   # push all lefts
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()            # visit node (inorder)
            k -= 1
            if k == 0:
                return cur.val

            cur = cur.right              # then go right