# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        def dfs(root):
            if not root:
                return 
            
            dfs(root.right)
            dfs(root.left)

            root.right = self.prev
            root.left = None
            self.prev = root
        
        dfs(root)
        return root

        