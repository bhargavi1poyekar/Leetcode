# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def createTree(low, high):

            if low>high:
                return None
            
            val=postorder.pop()
            root=TreeNode(val)
            idx=hash_idx[val]
            root.right=createTree(idx+1,high)
            root.left=createTree(low,idx-1)

            return root

        
        hash_idx={}
        for i in range(len(inorder)):
            hash_idx[inorder[i]]=i
        
        return createTree(0,len(inorder)-1)

       