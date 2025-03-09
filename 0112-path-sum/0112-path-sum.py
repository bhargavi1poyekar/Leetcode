# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, remainSum):
            if not root:
                return False

            if not root.left and not root.right:
                if remainSum == root.val:
                    return True
                
            return dfs(root.left, remainSum - root.val) or dfs(root.right, remainSum - root.val)
            
        return dfs(root, targetSum) 
            

