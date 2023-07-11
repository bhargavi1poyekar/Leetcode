# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        valid_paths=[]
        self.dfs(root,valid_paths,[],targetSum)
        return valid_paths

    def dfs(self, root, valid_paths, curr_path, remain_sum):

        if not root:
            return
        
        curr_path.append(root.val)
        # print(root.val,valid_paths,curr_path,remain_sum)

        if root.val==remain_sum and not root.left and not root.right:
            valid_paths.append(list(curr_path))
            
        else:
            self.dfs(root.left,valid_paths,curr_path,remain_sum-root.val)
            self.dfs(root.right,valid_paths,curr_path,remain_sum-root.val)


        curr_path.pop()
        return

        

        
    




