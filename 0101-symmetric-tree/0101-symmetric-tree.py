# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def checksame(p, q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            return p.val == q.val and checksame(p.left, q.right) and checksame(p.right, q.left)
        
        return checksame(root.left, root.right)
        
