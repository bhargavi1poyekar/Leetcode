# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, currsum):
            if not root:
                return False
            
            if not root.left and not root.right:
                if currsum + root.val == targetSum:
                    return True
            
            return dfs(root.left, currsum + root.val) or dfs(root.right, currsum + root.val)
        
        return dfs(root, 0)
