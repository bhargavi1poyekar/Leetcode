# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.maxsum = float('-inf')

        def dfs(root):
            if not root:
                return 0
            
            leftsum = max(0, dfs(root.left))
            rightsum = max(0, dfs(root.right))

            self.maxsum = max(self.maxsum, root.val + leftsum + rightsum)

            return max(root.val + leftsum, root.val + rightsum)
        
        dfs(root)
        return self.maxsum

