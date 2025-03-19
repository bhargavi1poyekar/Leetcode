# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def left_hght(root):
            if not root:
                return 0
            return 1 + left_hght(root.left)
        
        def right_hght(root):
            if not root:
                return 0
            return 1 + right_hght(root.right)
        
        if not root:
            return 0

        left_hght = 1 + left_hght(root.left)
        right_hght = 1 + right_hght(root.right)

        if left_hght == right_hght:
            return (2 ** left_hght) - 1

        elif left_hght > right_hght:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)        

