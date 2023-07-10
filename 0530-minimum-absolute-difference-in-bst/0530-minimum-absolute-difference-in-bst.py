# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        sorted_val=[]
        def inorder(root):
            if not root:
                return 

            inorder(root.left)
            sorted_val.append(root.val)
            inorder(root.right)
        
        inorder(root)

        min_abs=float('inf')
        for i in range(len(sorted_val)-1):
            min_abs=min(min_abs,sorted_val[i+1]-sorted_val[i])
        
        return min_abs

