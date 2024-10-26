# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def left_depth(root):
            if not root:return 0
            return 1+left_depth(root.left)

        def right_depth(root):
            if not root:return 0
            return 1+right_depth(root.right)
        
        if not root:
            return 0

        left_depth=1+left_depth(root.left)
        right_depth=1+right_depth(root.right)

        if left_depth==right_depth:
            return (2**left_depth)-1
        
        elif left_depth>right_depth:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)