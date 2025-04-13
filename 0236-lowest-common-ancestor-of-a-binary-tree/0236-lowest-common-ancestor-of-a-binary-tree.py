# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        '''
        Understand:

        Given binary tree -> return lowest common ancestor of given nodes. 
        lowest node, that has both p and q as descendants. 

        Match:
        dfs

        Plan:
        ok, so first of all, if any of the p, and q is root -> then it will be the lca -> because -> node can be descendant of itself. 

        now, if none of them is root. 
        we check in the left tree. 
        and check in right tree. 

        Now on both sides, if we get something. then one of them is in left and other in right. -> so we return root. 

        if only left, then both are on left, we return left. 
        otherwise right. 
        '''

        def dfs(root):
            if not root:
                return 
            
            if p == root or q == root:
                return root
            
            left = dfs(root.left)
            right = dfs(root.right)

            if left and right:
                return root
            if left:
                return left
            return right
    
        return dfs(root)

        '''
        Time Complexity -> O(n)
        Space -> O(n) -> stack overhead.
        '''
            

        