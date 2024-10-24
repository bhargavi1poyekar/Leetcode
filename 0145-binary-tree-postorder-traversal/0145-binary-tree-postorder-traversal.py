# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        list_order = []
        def prot(root):
            if not root:
                return
            
            prot(root.left)
            prot(root.right)
            list_order.append(root.val)
        
        prot(root)
        return list_order