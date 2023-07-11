# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        longestpath=0

        def dfs(root,parentLeft,steps):
            nonlocal longestpath
            if root:
                longestpath=max(longestpath,steps)

                if parentLeft:
                    dfs(root.left,True,1)
                    dfs(root.right,False,steps+1)
                else:
                    dfs(root.left,True,steps+1)
                    dfs(root.right,False,1)

        
        dfs(root,False,0)
        dfs(root,True,0)
        return longestpath
                