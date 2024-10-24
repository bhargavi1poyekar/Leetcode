# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def minimum_dep(root):
            if not root:
                return 0
            if not root.left:
                return minimum_dep(root.right) + 1
            if not root.right:
                return minimum_dep(root.left) + 1
            
            return min(minimum_dep(root.left), minimum_dep(root.right)) + 1
            
        return minimum_dep(root)

       