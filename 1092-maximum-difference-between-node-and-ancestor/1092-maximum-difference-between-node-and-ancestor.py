# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def max_diff(root, curr_max, curr_min):
            if not root:
                return curr_max - curr_min
            
            left_diff = max_diff(root.left, max(curr_max, root.val), min(curr_min, root.val))
            right_diff = max_diff(root.right, max(curr_max, root.val), min(curr_min, root.val))
            return max(left_diff, right_diff)
        
        return max_diff(root, root.val, root.val)