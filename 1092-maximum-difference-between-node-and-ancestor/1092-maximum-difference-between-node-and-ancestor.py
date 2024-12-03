# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(root, maxval, minval):
            if not root:
                return maxval - minval
            
            left = dfs(root.left, max(root.val, maxval), min(root.val, minval))
            right = dfs(root.right, max(root.val, maxval), min(root.val, minval))

            return max(left, right)

        return dfs(root, root.val, root.val)

        