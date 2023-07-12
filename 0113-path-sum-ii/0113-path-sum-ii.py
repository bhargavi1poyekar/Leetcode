# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        valid_paths=[]
       

        def dfs(root,curr_path, remain_sum):

            if not root: # If no root return
                return
            
            curr_path.append(root.val) # add current node in curr_path
            
            # if curr node is equal to remain sum for target, and if lead node
            if root.val==remain_sum and not root.left and not root.right: 
                valid_paths.append(list(curr_path)) # append curr path to valid paths
                
            else:
                # if not leaf node, go to left or right
                dfs(root.left,curr_path,remain_sum-root.val) 
                dfs(root.right,curr_path,remain_sum-root.val)

            # Remove curr node from curr_path
            curr_path.pop()
            
        
       
        dfs(root,[],targetSum)
        return valid_paths

        

        
    




