# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        self.hash_sum = Counter()
        self.hash_sum[0] = 1
        self.num_paths = 0

        def dfs(root, curr_sum):
            if not root:
                return 

            curr_sum += root.val
            self.num_paths += self.hash_sum[curr_sum - targetSum] 
            self.hash_sum[curr_sum] += 1

            dfs(root.left, curr_sum)
            dfs(root.right, curr_sum)

            self.hash_sum[curr_sum] -= 1

            return 
        
        dfs(root, 0)
        return self.num_paths
            
            

            