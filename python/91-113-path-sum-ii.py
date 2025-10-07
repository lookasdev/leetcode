# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(N * H) → worst O(N^2), average O(N logN)
    # Space: O(N * H) (for result + recursion depth)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []

        def dfs(node, path, sumSoFar):
            sumSoFar += node.val
            pathSoFar = path + [node.val]
            if node.left:
                dfs(node.left, pathSoFar, sumSoFar)
            if node.right:
                dfs(node.right, pathSoFar, sumSoFar)
            if not node.left and not node.right and sumSoFar == targetSum:
                output.append(pathSoFar)

        if not root: 
            return []
        dfs(root, [], 0)
        return output