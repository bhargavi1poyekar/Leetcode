# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list_order = []
        def iot(root):
            if not root:
                return
            iot(root.left)
            list_order.append(root.val)
            iot(root.right)
        
        iot(root)
        return list_order