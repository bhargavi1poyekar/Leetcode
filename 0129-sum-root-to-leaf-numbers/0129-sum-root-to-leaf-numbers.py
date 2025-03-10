# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.paths = []

        def dfs(root, op):
            if not root:
                return 
            
            if not root.left and not root.right:
                op = op * 10 + root.val
                self.paths.append(op)
            
            dfs(root.left, op*10 + root.val)
            dfs(root.right, op*10 + root.val)
        
        dfs(root, 0)
        return sum(self.paths)