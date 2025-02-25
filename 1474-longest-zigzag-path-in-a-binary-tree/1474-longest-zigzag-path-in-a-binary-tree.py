# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        self.longest = 0

        def dfs(root, Left, curr_length):
            if not root:
                return
            
            self.longest = max(curr_length, self.longest)

            if Left:
                dfs(root.left, 1, 1)
                dfs(root.right, 1, curr_length + 1)
            else:
                dfs(root.left, 0, curr_length + 1)
                dfs(root.right, 0, 1)

            return

        dfs(root, 1, 1)
        dfs(root, 0, 1) 

        return self.longest-1
