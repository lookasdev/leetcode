# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # using a “global” (really: outer, mutable) variable
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]   # outer mutable to track the best seen anywhere

        def dfs(node):
            if not node:
                return 0

            leftMax  = dfs(node.left)
            rightMax = dfs(node.right)

            # a parent can only extend one side; drop negatives
            leftMax  = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # consider a split at this node (left + node + right)
            res[0] = max(res[0], node.val + leftMax + rightMax)

            # return the best downward (no-split) path to parent
            return node.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]

    # no outer variable; dfs returns two numbers
    # def maxPathSum(self, root: TreeNode) -> int:

    #     def dfs(node):
    #         if not node:
    #             # with-split is -inf so it won't affect maxima; downward is 0 (extend nothing)
    #             return (float('-inf'), 0)

    #         left_with,  left_down  = dfs(node.left)
    #         right_with, right_down = dfs(node.right)

    #         # drop negatives for paths we extend upward
    #         left_down  = max(left_down, 0)
    #         right_down = max(right_down, 0)

    #         # path that splits at this node (left + node + right)
    #         through = node.val + left_down + right_down

    #         # best path anywhere in this subtree (maybe in left/right, maybe through here)
    #         best_with_split = max(left_with, right_with, through)

    #         # best downward (no-split) path starting at this node for parent to extend
    #         best_down = node.val + max(left_down, right_down)

    #         return (best_with_split, best_down)

    #     best_with, _ = dfs(root)
    #     return best_with