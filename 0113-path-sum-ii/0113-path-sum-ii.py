# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        valid_paths = []

        def dfs(root, remainingSum, currpath):

            if not root:
                return None
            
            currpath.append(root.val)

            if not root.left and not root.right:
                if root.val == remainingSum:
                    valid_paths.append(currpath[:])

            if root.left:
                dfs(root.left, remainingSum - root.val, currpath)
            if root.right:
                dfs(root.right, remainingSum - root.val, currpath)
            
            currpath.pop()
            return 
        
        dfs(root, targetSum, [])
        return valid_paths