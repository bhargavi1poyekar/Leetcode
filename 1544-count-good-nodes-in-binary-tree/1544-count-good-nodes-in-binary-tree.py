# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxval):
            if not root:
                return 0
            
            left = dfs(root.left, max(maxval, root.val))
            right = dfs(root.right, max(maxval, root.val))

            if root.val >= maxval:
                return 1 + left + right
            return left + right
        
        return dfs(root, root.val)