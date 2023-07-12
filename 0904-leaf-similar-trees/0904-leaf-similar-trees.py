# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def checkleaves(root):
            
            if not root: return []
            if root:
                if not root.left and not root.right:
                    return [root.val]
                
                checkleaves(root.left)
                checkleaves(root.right)

            return checkleaves(root.left)+checkleaves(root.right)
        
        # print(checkleaves(root1))
        return checkleaves(root1)==checkleaves(root2)
                    
            
