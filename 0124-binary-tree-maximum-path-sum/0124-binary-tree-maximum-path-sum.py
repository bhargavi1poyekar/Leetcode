# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.maxpath = float('-inf')
        def dfs(root):
            if not root:
                return 0
            
            leftGain = max(0, dfs(root.left))
            rightGain = max(0, dfs(root.right))

            self.maxpath = max(self.maxpath, leftGain + root.val + rightGain)

            return max(leftGain + root.val, rightGain + root.val)
        
        dfs(root)
        return self.maxpath