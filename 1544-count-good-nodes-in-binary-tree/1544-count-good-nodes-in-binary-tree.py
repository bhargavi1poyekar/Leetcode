# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, maxnode):

            if not root:
                return 0
            
            leftgood=dfs(root.left,max(root.val,maxnode))
            rightgood=dfs(root.right,max(root.val,maxnode))
            ans=leftgood+rightgood

            if root.val>=maxnode:
                ans+=1
            return ans
        
        return dfs(root,float('-inf'))