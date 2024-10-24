# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lca(root, p, q):
            if not root:
                return None
            if p == root or q == root:
                return root
            
            leftlca = lca(root.left, p, q)
            rightlca = lca(root.right, p, q)

            if leftlca and rightlca:
                return root
            if leftlca:
                return leftlca
            return rightlca

        return lca(root, p, q)