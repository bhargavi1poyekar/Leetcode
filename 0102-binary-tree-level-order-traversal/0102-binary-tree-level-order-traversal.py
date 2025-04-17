# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Understand:

        Given root -> return level order traversal. 
        left to right level by level. 

        Match: BFS -> using queue.

        Plan:
        add root to queue. 
        now at every level, 
        popleft queue -> add to the level. 

        and add the node.left and node.right to the queue if exist. 
        COntinue till queue is empty. 
        '''

        if not root:
            return []

        queue = deque([root])

        level_order_trav = []

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            level_order_trav.append(level)
        
        return level_order_trav

        '''
        Time COmplexity: O(n)
        Space complexitY: O(N)
        '''