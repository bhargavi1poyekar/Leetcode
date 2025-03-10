# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, maxnode):
            if not root:
                return 0

            left_good = dfs(root.left, max(maxnode, root.val))
            right_good = dfs(root.right, max(maxnode, root.val))

            if root.val >= maxnode:
                return 1 + left_good + right_good
            return left_good + right_good

        return dfs(root, root.val)                
            
