# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def ancestor(root, maxval, minval):
            if not root:
                return maxval - minval
            
            left = ancestor(root.left, max(maxval, root.val), min(minval, root.val))
            right = ancestor(root.right, max(maxval, root.val), min(minval, root.val))
            return max(left, right)
        
        return ancestor(root, root.val, root.val)






        