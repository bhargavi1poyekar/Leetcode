# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preord(root):
            if not root:
                return 
            ans.append(root.val)
            preord(root.left)
            preord(root.right)
            return ans
        
        ans=[]
        ans=preord(root)
        return ans