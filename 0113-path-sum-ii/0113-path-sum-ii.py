# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        valid_paths = [] 
        def path_sum(root, curr_path, remain_sum):
            if not root:
                return 
            
            curr_path.append(root.val)
            if not root.left and not root.right:
                if remain_sum == root.val:
                    valid_paths.append(list(curr_path))
            
            path_sum(root.left, curr_path, remain_sum - root.val)
            path_sum(root.right, curr_path, remain_sum - root.val)

            curr_path.pop()
        
        path_sum(root, [], targetSum)
        return valid_paths