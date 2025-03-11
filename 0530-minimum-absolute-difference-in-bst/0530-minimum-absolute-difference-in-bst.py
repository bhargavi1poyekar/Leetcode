# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        sorted_array = inorder(root)
        # print(sorted_array)

        min_diff = float('inf')

        for i in range(len(sorted_array) - 1):
            diff = abs(sorted_array[i] - sorted_array[i+1])
            min_diff = min(min_diff, diff)

        return min_diff 
