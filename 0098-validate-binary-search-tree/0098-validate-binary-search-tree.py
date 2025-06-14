# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, maxval, minval):
            if not root:
                return True
            
            if not (minval < root.val < maxval):
                return False
            
            return dfs(root.left, root.val, minval) and dfs(root.right, maxval, root.val)
        
        return dfs(root, float('inf'), float('-inf'))