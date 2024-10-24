# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        inorder_list = []
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            inorder_list.append(root.val)
            inorder(root.right)

        inorder(root)
        return inorder_list[1] - inorder_list[0]