# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        '''
        Understand: 

        Given a root -> check if valid binary search tree. 

        Left subtree nodes _> less than nodes key, 
        right subtree -> greater than. 

        Match: DFS

        Plan:

        while traversing, we also set max val and min val. 

        So like, starting from root -> max and min would be infinte ends. 

        But while going to left of root -> max would be root -> because the left nodes should be less than root. 

        similarly while going right -> change min to root. 

        Continue this and return if any of the node invalidates the constraint.
        '''

        def dfs(root, max, min):
            if not root:
                return True
            
            if root.val >= max or root.val <= min:
                return False

            return dfs(root.left, root.val, min) and dfs(root.right, max, root.val)

        return dfs(root, float('inf'), float('-inf'))

        '''
        Time Complexity: O(N)
        Space COmplexity: O(1) => O(N) -> for stack overhead. 
        '''