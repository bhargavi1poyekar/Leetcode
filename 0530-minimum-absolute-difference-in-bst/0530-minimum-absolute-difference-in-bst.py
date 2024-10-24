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

        min_abs=float('inf')
        for i in range(len(inorder_list)-1):
            min_abs=min(inorder_list[i+1]-inorder_list[i], min_abs)
        
        return min_abs