# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        preorder = deque(preorder)

        def dfs(low, high):
            if low >= high:
                return None
            
            val = preorder.popleft()
            node = TreeNode(val)

            idx = hash_idx[val]
            node.left = dfs(low, idx)
            node.right = dfs(idx + 1, high)

            return node

        hash_idx = {}        
        for i in range(len(inorder)):
            hash_idx[inorder[i]] = i
        
        return dfs(0, len(inorder))




        