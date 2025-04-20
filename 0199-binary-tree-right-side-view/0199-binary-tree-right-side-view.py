# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        '''
        Understand:

        Given root -> return values that can be seen from the right side. 

        Last element of a level. 

        Match: BFS traversal on tree. 

        Plan:
        at every level, once you finish the iteration, append the last element to final answer. 
        '''
        if not root:
            return []
            
        queue = deque([root])
        rsv = []
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            rsv.append(node.val)
    
        return rsv

        '''
        Time Complexity: O(N)
        Space COmplexity: O(h)
        '''
                