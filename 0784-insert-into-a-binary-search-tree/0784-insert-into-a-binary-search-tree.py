# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            node=TreeNode(val)
            return node

        if root.val>val and root.left:
            self.insertIntoBST(root.left,val)
        elif root.val<val and root.right:
            self.insertIntoBST(root.right,val)
        
        elif root.val>val and not root.left:
            newnode=TreeNode(val)
            root.left=newnode
        elif root.val<val and not root.right:
            newnode=TreeNode(val)
            root.right=newnode
            
        return root



