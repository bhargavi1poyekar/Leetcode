# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return True, 0

            left_bal, left_ht = dfs(root.left)
            if not left_bal:
                return False, 0
            
            right_bal, right_ht = dfs(root.right)
            if not right_bal:
                return False, 0
            
            return abs(right_ht - left_ht) <= 1, 1+ max(left_ht, right_ht)
        
        return dfs(root)[0]
                
        

        
        