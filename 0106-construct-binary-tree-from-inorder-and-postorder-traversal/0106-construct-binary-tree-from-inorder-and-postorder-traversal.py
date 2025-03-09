# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index_hash = {}

        for i in range(len(inorder)):
            index_hash[inorder[i]] = i
        
        def construct(left, right):
            if left >= right:
                return None
            
            val = postorder.pop()
            node = TreeNode(val)

            index = index_hash[val]
            node.right = construct(index+1, right)
            node.left = construct(left, index)
        
            return node
        
        return construct(0, len(inorder))