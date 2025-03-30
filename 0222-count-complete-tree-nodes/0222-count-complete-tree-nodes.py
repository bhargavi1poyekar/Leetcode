# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def left_ht(root):
            if not root:
                return 0
            return 1 + left_ht(root.left)
        
        def right_ht(root):
            if not root:
                return 0
            return 1 + right_ht(root.right)
        
        if not root:
            return 0
        
        left_ht = 1 + left_ht(root.left)
        right_ht = 1 + right_ht(root.right)

        if left_ht == right_ht:
            return (2 ** left_ht) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
        