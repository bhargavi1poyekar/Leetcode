# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # self.idx = 0
        preorder = deque(preorder)
        def createTree(left_bound, right_bound):
            if left_bound > right_bound:
                return None
            
            val  = preorder.popleft()
            # self.idx += 1

            root = TreeNode(val)
            index = hash_idx[val]

            root.left = createTree(left_bound, index-1)
            root.right = createTree(index+1, right_bound)

            return root
        
        hash_idx = {}
        for i in range(len(inorder)):
            hash_idx[inorder[i]] = i
        
        return createTree(0, len(inorder)-1)