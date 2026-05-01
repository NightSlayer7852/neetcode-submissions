# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, value):
            if not root:
                return 0
            
            if root.val >= value:
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
            else:
                return dfs(root.left, value) + dfs(root.right, value)
        return dfs(root, -101)