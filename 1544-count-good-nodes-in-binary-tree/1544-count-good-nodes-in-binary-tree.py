# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.goodnodes = 0
        def dfs(root, maxval):
            if not root:
                return 0
            
            if root.val >= maxval:
                self.goodnodes += 1
            
            dfs(root.left, max(maxval, root.val))
            dfs(root.right, max(maxval, root.val))
        
        dfs(root, root.val)
        return self.goodnodes

            