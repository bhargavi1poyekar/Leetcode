# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        '''
        Understood:

        Given root of BST and k. 
        Return -> kth smallest value (for 0 index -> k-1)   

        Match:
        inorder -> inorder -> gives sorted list of a BST Tree
        
        Plan:
        Get the sorted list of BST by performing inorder on the tree 
        Return k-1 st index element in the list. 

        '''
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        return inorder(root)[k-1]

        '''
        Time complexity: O(n) -> traversing all the nodes. 
        Space: O(n) -> sorted list
        '''