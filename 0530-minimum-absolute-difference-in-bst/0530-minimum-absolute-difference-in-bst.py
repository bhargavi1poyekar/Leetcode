# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(root):
            if not root: return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        sorted_arr = inorder(root)

        min_abs_diff = float('inf')
        for i in range(1, len(sorted_arr)):
            diff = abs(sorted_arr[i] - sorted_arr[i-1])
            min_abs_diff = min(diff, min_abs_diff)

        return min_abs_diff 