"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        '''
        Understand: Populate next pointer -> to its right node. in the same level. 
        no right node -> set to Null. 

        Match: BFS -> traverse level by level

        Plan:
        for BFS, once we add the root:
        
        while queue:
            store length of queue
            add NULL pointer in the queue. 
            
            for each node in queue (stored length):
                node = popleft
                node.right = queue[0]

                add left and right nodes if exist to the queue. 
            
            popleft the null pointer. 
        
        return the root. 
        '''
        # if empty root -> return empty list 
        if not root:
            return root
        
        queue = deque([root])

        while queue:
            length = len(queue)

            # Add Null pointer at end of queue. 
            queue.append(None)

            for _ in range(length):
                node = queue.popleft()

                # add the next pointer to the next right node in a level
                node.next = queue[0]
            
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            # Remove null pointer. 
            queue.popleft()
        
        return root
        '''
        Time Complexity -> O(N)
        Space -> O(n)
        '''



        