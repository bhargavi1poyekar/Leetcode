# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.total_sum = 0
        def dfs(root, num):
            if not root:
                return 
            num = num * 10 + root.val
            if not root.left and not root.right:
                self.total_sum += num
            
            dfs(root.left, num)
            dfs(root.right, num)
        
        dfs(root, 0)
        return self.total_sum

