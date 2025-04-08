# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        '''
        Understand:

        Given -> root

        Zigzag -> right or left. if move to diff direction => +1
        if same direction -> new path. 
        Single node -> length of 0

        Return longest path -> length of the path. 

        Match:
        Dfs in a tree. at every point go to left or right. 

        Plan:

        current node -> start with root -> we have 2 options -> go left or right. 
        we will explore both options. 
        and keep on updating the max length. 

        ok, so for dfs

        function(root, current direction, currlength)

        curr direction means -> from parent did we come left or right. 
        and curr length -> length of the path. 
        so at each node. if root doesnt exist we just return. 
        otherwise. We update the max_length. 

        Now based of curr direction
        if Left:
            goLeft(root.left, left, 1) -> curr length again starts from 1. 
            goRight(root.right, right, currlength + 1)
        if Right:
            goLeft(root.left, left, currlength + 1) -> curr length again starts from 1. 
            goRight(root.right, right, 1)
        '''
        # Implement

        # Left -> True means -> curr direction is left, else right

        self.max_length = 0

        def dfs(root, Left, curr_length):
            if not root:
                return 
            
            self.max_length = max(self.max_length, curr_length)

            if Left:
                dfs(root.left, True, 1)
                dfs(root.right, False, curr_length + 1)
            else:
                dfs(root.left, True, curr_length + 1)
                dfs(root.right, False, 1)
        
            return
    
        dfs(root, True, 0)
        dfs(root, False, 0)
        return self.max_length

        '''
        Evaluate:

        Time Complexity: O(n)
        Space Complexity: O(n) -> stack overhead. 
        '''

