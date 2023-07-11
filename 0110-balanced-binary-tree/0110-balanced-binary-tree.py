# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        def depth(root):
            if not root:
                return 0
            left=depth(root.left)
            right=depth(root.right)
            return 1+max(left,right)
        
        left_height=depth(root.left)
        right_height=depth(root.right)

        left_balance=self.isBalanced(root.left)
        right_balance=self.isBalanced(root.right)

        return abs(left_height-right_height)<=1 and left_balance and right_balance

