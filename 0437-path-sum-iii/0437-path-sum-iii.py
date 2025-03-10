# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        self.num_paths = 0
        self.hash = Counter()
        self.hash[0] = 1 # -> very important. 

        def dfs(root, curr_sum):
            if not root:
                return 
            
            curr_sum += root.val
            # if (curr_sum - targetSum) in self.hash:
            self.num_paths += self.hash[curr_sum - targetSum]
            
            self.hash[curr_sum] += 1
            
            dfs(root.left, curr_sum)
            dfs(root.right, curr_sum)

            self.hash[curr_sum] -= 1
        
        dfs(root, 0)
        return self.num_paths
        
