# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        self.count = 0
        self.paths = Counter()
        self.paths[0] = 1


        def dfs(root, currsum):
            if not root:
                return
            
            currsum += root.val
            self.count += self.paths[currsum - targetSum]
            self.paths[currsum] += 1

            dfs(root.left, currsum)
            dfs(root.right, currsum)

            self.paths[currsum] -= 1
            return 
        
        dfs(root, 0)
        return self.count