# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(root,curr_sum):
            if not root:
                return False
            
            if not root.left and not root.right:
                return curr_sum+root.val==targetSum

            curr_sum+=root.val
            left=dfs(root.left,curr_sum)
            right=dfs(root.right,curr_sum)

            return left or right
        
        return dfs(root,0)
