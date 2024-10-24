# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def check_same(p, q):
            if not p and not q:
                return True
            if not p:
                return False
            if not q:
                return False
            
            return p.val == q.val and check_same(p.right, q.right) and check_same(p.left, q.left)
            
        return check_same(p, q)