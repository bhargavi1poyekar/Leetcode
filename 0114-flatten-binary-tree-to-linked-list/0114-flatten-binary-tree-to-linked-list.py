# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        '''
        Understand:

        Given -> root we need to flatten the tree. 
        So we need to convert all the left to right -> and it needs to be the same preorder. 

        Match: with given tree -> i woull like to perform reverse preorder using dfs. 

        preorder -> visit, left, right
        reverse -> right, left, visit. 

        Plan:

        in dfs() follow reverse preorder -> and alwyas visit the right node first. 

        then assign a temp pointer -> prev, initialized to None
        Now, we assign the right of node as prev. 
        And make the left as none. 

        then we make the current node as prev. 

        how this works:

        prev -> 1

        root = 6
        root.right = prev -> None
        roo.left = None

        root = 5
        root.right = prev -> 6
        root.left = None

        root = 4
        root.right = prev -> 5
        root.left = None
        
        root = 3
        root.right = prev -> 4
        root.left = None

        root = 2
        root.right = prev -> 3 
        
        root = 1 
        root.right = prev -> 2

        then return root. 
        '''
        self.prev_root = None
        def dfs(root):
            if not root:
                return
            
            # Reverse Preorder
            dfs(root.right)
            dfs(root.left)

            # Visit
            # assign prev root to right, and left as None. 
            root.right = self.prev_root
            root.left = None

            # and then make curr root as prev root
            self.prev_root = root
        
        dfs(root) # Do dfs
        return root

        '''
        Evaluate -> O(n) -> traversing all the nodes. 
        Space -> O(1)
        '''

            
        