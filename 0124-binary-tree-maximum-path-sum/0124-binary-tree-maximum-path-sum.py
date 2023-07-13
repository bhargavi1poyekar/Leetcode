# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxSum=float('-inf')
        def pathGain(root):
            if not root:
                return 0

            nonlocal maxSum
            left_gain=max(0,pathGain(root.left))
            right_gain=max(0,pathGain(root.right))

            maxSum=max(maxSum,root.val+left_gain+right_gain)

            return max(root.val+left_gain,root.val+right_gain)
        
        pathGain(root)
        return maxSum