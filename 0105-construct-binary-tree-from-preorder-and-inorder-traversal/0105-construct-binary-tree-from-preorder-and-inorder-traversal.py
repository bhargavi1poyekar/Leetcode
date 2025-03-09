# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        preorder = deque(preorder)
        index_hash = {}

        for i in range(len(inorder)):
            index_hash[inorder[i]] = i
        
        def construct(left, right):
            if left >= right:
                return None
            
            val = preorder.popleft()
            node = TreeNode(val)

            index = index_hash[val]
            node.left = construct(left, index)
            node.right = construct(index+1, right)
        
            return node
        
        return construct(0, len(inorder))









