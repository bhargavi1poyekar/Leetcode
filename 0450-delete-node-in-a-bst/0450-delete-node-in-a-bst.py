# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def findmin(root):
            while root.left:
                root = root.left
            return root.val
        
        def findmax(root):
            while root.right:
                root = root.right
            return root.val
        
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.right:
                root.val = findmin(root.right)
                root.right = self.deleteNode(root.right, root.val)
            elif root.left:
                root.val = findmax(root.left)
                root.left = self.deleteNode(root.left, root.val)
        
        return root
