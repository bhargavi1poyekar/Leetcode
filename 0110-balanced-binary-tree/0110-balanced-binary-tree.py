# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            # if null node:
            if not root:
                return True, 0 # height is balanced and 0
            
            # Check left subtree -> if not balanced return False
            left_balance, left_ht = dfs(root.left)
            if not left_balance:
                return False, 0

            # Check right subtree -> if not balanced return False
            right_balance, right_ht = dfs(root.right)
            if not right_balance:
                return False, 0

            
            # if left and right subtree are balanced, now check balance of curr node. and return height of curr node.  
            return abs(left_ht - right_ht) <= 1, 1+ max(left_ht, right_ht)
        
        return dfs(root)[0] # 0th index tells true of false for balanced