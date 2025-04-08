# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        '''
        Understand:

        Given root. 
        we need to invert. all left needs to be right. give mirror image of the current tree. 
        empty tree -> return empty

        Match:
        dfs. 

        Plan:
        at every dfs -> just swap left and right. and do the same for left child, as well as right child. 
        '''

        def dfs(root):
            if not root:
                return

            root.left, root.right = root.right, root.left
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return root

        '''
        Time Complexity -> O(n)
        Space Complexity -> O(h) -> stack overhead. h function calls. in worst case 
        '''