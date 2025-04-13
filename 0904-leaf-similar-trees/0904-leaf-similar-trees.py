# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        '''
        Understand:

        Given: roots of 2 trees
        get list of leaves of binary tree from left to right. 

        Return if both trees have same leaves in the same order. 

        Match:
        dfs on the tree -> get leaves

        Plan:
        Perform dfs on both trees. Get list of leaves of the trees. 
        Compare both lists. 
        '''

        # Implmentation. 

        def dfs(root):
            if not root:
                return []
            # Check if leaves, if yes, then return them in a list
            if not root.left and not root.right:
                return [root.val]
            
            # Concatenate the left and right leaves.
            return dfs(root.left) + dfs(root.right)
        
        # Compare list of leaves of both trees. 
        return dfs(root1) == dfs(root2)

        '''
        Time Complexity: O(M + N) -> M: num nodes in tree1 and N: num nodes in tree 2

        Space Complexity: O(M + N) -> stack overhead and leaves list. 
        '''
