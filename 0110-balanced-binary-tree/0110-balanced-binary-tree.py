# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> (bool,int):

        def bottom_up(root):
            if not root:
                return True,0

            # def depth(root):
            #     if not root:
            #         return 0
            #     left=depth(root.left)
            #     right=depth(root.right)
            #     return 1+max(left,right)
            
            left_balance,left_height=bottom_up(root.left)

            if not left_balance:
                return False,0
            right_balance,right_height=bottom_up(root.right)

            if not right_balance:
                return False,0

            return abs(left_height-right_height)<=1, 1+max(left_height,right_height)
        
        
        return(bottom_up(root)[0])

