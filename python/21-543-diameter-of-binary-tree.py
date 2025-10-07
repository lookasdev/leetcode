# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return -1  # return -1 so leaf nodes have height 0

            left = dfs(root.left)
            right = dfs(root.right)

            # Update diameter at this node
            res[0] = max(res[0], 2 + left + right)

            # Return height of this subtree
            return 1 + max(left, right)

        dfs(root)
        return res[0]