# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # if not root:
        #     return True
        # def traverse(l,r):
        #     if not l and not r:
        #         return True
        #     if not l or not r:
        #         return False
        #     if l.val ==r.val:
        #         return traverse(l.left,r.right) and traverse(l.right,r.left)
        #     return False
        
        # return traverse(root.left, root.right)

        if not root:
            return True

        def dfs(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val==q.val and dfs(p.left,q.right) and dfs(p.right,q.left)
        
        return dfs(root.left, root.right)