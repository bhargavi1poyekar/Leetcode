# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        preorder = deque(preorder)
        self.inorder_to_index = {}

        def makeTree(left, right):
            if left >= right:
                return None
            
            val = preorder.popleft()
            root = TreeNode(val)

            index = self.inorder_to_index[val]

            root.left = makeTree(left, index)
            root.right = makeTree(index+1, right)
        
            return root
        
        for i, val in enumerate(inorder):
            self.inorder_to_index[val] = i
        
        return makeTree(0, len(inorder))