# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def left_depth(root):
            if not root: return 0
            return 1 + left_depth(root.left)

        def right_depth(root):
            if not root: return 0
            return 1 + right_depth(root.right)

        if not root:
            return 0
        
        leftDepth = 1 + left_depth(root.left)
        rightDepth = 1 + right_depth(root.right)
        
        if leftDepth == rightDepth:
            return (2 ** leftDepth) - 1
        return 1+ self.countNodes(root.left) + self.countNodes(root.right)
        