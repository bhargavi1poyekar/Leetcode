# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        '''
        Understand:
        Given -> root. 

        we need to find max path sum -> path does not need to go through root.

        Values can be negative. 

        Match-> Tree dfs. 

        Plan:

        at every node. we check what maxsum we get from left, and what from right.
        If maxsum from left or right is negative, we just keep it as 0. 

        Then update maxpath with max of curr path sum. 
        curr path is like leftGain + rightGain + root.val

        now we return the maxpath from either left, or right.
        '''
        
        self.maxpath = float('-inf')

        def dfs(root):
            if not root:
                return 0
            
            leftGain = max(0, dfs(root.left))
            rightGain = max(0, dfs(root.right))
            self.maxpath = max(self.maxpath, leftGain + rightGain + root.val)
            return max(leftGain + root.val, rightGain + root.val)
        
        dfs(root)
        return self.maxpath
