# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Understand:

        Given root -> return max depth. 
        max_depth -> num nodes along longest path (root to leaf)

        if no root -> 0
        if only root -> 1

        Match: Can do a dfs to find the depths. 

        Plan:

        dfs(root):

            if not root:
                return 0

            left_depth = dfs(left)
            rightdepth = dfs(right)

            return 1 (adding depth of root) + max(left, right)

        at any junction -> we have 2 choices -> take either left depth and consider that path, or take right depth with that path. 

        So we choose max of it. 
        '''
        # Implement
        def dfs(root):
            if not root:
                return 0
            
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)

            return 1 + max(left_depth, right_depth)
        
        return dfs(root)

        '''
        Review:
        since we are using postorder traversal. 
        lets start from leaf nodes. 

        9 -> returns 1 + max(0, 0) -> 1
        15 -> returns 1 + max(0, 0) -> 1
        7 -> returns 1 + max(0, 0) -> 1

        20 -> returns 1 + max(1, 1) -> 2

        root -> 3 returns 1 + max(1, 2) -> 3

        Evaluate:
        Time Complexity: O(n) -> we traverse each node. 
        Space Complexity: O(1) -> O(n) -> stack overhead in recursion.
        '''



