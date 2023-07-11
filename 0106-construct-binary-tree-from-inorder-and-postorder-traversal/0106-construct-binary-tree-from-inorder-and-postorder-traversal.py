# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def createTree(left_bound,right_bound):

            if left_bound>right_bound:
                return None
            
            val=postorder.pop()
            root=TreeNode(val)
            index=hash_idx[val]

            root.right=createTree(index+1,right_bound)
            root.left=createTree(left_bound,index-1)

            return root
        
        hash_idx={}
        for i in range(len(inorder)):
            hash_idx[inorder[i]]=i

        return createTree(0,len(inorder)-1)
