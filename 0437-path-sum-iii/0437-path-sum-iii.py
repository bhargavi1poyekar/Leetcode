# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(root,curr_sum):

            if not root:
                return
            
            nonlocal count
            curr_sum+=root.val

            count+=prefix_hash[curr_sum-targetSum]
            prefix_hash[curr_sum]+=1
            
            dfs(root.left,curr_sum)
            dfs(root.right,curr_sum)

            prefix_hash[curr_sum]-=1
            
            
       
        count,curr_sum=0,0
        prefix_hash=Counter()
        prefix_hash[0]=1
        dfs(root,curr_sum)
        return count
    
    

