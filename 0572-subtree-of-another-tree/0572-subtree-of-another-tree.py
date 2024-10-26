# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check_same(p, q):
            if not p and not q:
                return True
            
            if not p or not q:
                return  False

            return p.val == q.val and check_same(p.left, q.left) and check_same(p.right, q.right)

        def dfs(root):
            if not root:
                return False
            elif check_same(root, subRoot): return True
            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)