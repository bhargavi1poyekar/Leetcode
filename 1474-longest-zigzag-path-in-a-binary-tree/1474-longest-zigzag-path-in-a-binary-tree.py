# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        self.longest = 0

        def dfs(root, L, count):
            if not root:
                return 
            self.longest = max(count, self.longest)
            
            if L:
                dfs(root.left, True, 1)
                dfs(root.right, False, count+1)
            else:
                dfs(root.left, True, count+1)
                dfs(root.right, False, 1)
        
        dfs(root, True, 0)
        dfs(root, False, 0)

        return self.longest
            

            