# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_node):
            if not root:
                return 0
            
            left = dfs(root.left, max(max_node, root.val))
            right = dfs(root.right, max(max_node, root.val))

            if root.val >= max_node:
                return 1 + left +  right
            return left + right
        
        return dfs(root, root.val)

            










        