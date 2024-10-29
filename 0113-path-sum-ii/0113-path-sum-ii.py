# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        def path_sum(root, remaining_sum, curr_path):
            if not root:
                return None
            
            curr_path.append(root.val)
            if not root.left and not root.right:
                if root.val - remaining_sum == 0:
                    paths.append(curr_path[:])

            if root.left:
                path_sum(root.left, remaining_sum - root.val, curr_path)
            
            if root.right:
                path_sum(root.right, remaining_sum - root.val, curr_path)
            
            curr_path.pop()
            return
        
        path_sum(root, targetSum, [])
        return paths

