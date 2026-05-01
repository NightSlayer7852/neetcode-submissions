# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")
        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            maxPath = left + node.val + right
            self.res = max(self.res, maxPath)
            return max(left + node.val, node.val + right)
        dfs(root)
        return self.res