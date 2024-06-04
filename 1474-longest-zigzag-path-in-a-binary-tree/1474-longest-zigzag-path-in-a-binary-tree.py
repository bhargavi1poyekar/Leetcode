# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest=0

        def dfs(root,curr_left,curr_path):
            if not root:
                return 
            
            self.longest=max(self.longest,curr_path)
            
            if curr_left:
                dfs(root.left,True,1)
                dfs(root.right,False,curr_path+1)
            else:
                dfs(root.left,True,curr_path+1)
                dfs(root.right,False,1)
            
        dfs(root,True,0)
        dfs(root,False,0)
        return self.longest