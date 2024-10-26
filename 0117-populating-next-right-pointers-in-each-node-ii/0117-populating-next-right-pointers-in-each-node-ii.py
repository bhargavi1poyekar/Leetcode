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

        if not root:
            return None
        
        Q = deque([root])

        while Q:
            length = len(Q)
            Q.append(None)

            for _ in range(length):
                node = Q.popleft()
                node.next = Q[0]

                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
 
            Q.popleft()
        return root
        