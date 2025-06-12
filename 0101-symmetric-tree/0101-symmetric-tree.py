# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isSame(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            
            return p.val == q.val and isSame(p.right, q.left) and isSame(p.left, q.right)
        
        return isSame(root.left, root.right)
