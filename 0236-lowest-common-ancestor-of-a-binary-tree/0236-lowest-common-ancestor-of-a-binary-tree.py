# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Base Case
        if not root:
            return None

        # First Case => if one of them is root, LCA cannot be after this.
        if p==root or q==root:
            return root

        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)

        # If both left right return something, then one of p and q is in left and other in right
        if left and right:
            return root 
        
        # if only one of them return something, both p and q are present in the same subtree.
        if left:
            return left
        
        return right
