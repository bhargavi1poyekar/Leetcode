# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def checksame(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and checksame(p.left, q.left) and checksame(p.right, q.right)
        
        def dfs(root):
            if not root:
                return False
            elif checksame(root, subRoot):
                return True
            
            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)