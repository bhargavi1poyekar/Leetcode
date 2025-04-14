# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        '''
        Understand:

        Given root -> return average val of nodes on each level.

        Match: BFS traversal

        Plan:
        add root to queue. 

        avg_list = []

        while queue. 
            list of node vals
            for each node in queue
                pop node
                add node val to list
                add left and right nodes if exist. 
            
            calculate avg of list and add to the avg list.
        
        return avg list. 
        '''

        # Implementation

        queue = deque([root])

        avg_list = []
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            avg_list.append(sum(level) / len(level))

        return avg_list 

        '''
        Time Complexity: O(n)
        Space: O(n)
        '''