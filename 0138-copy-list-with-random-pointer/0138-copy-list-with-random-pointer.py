"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
            
        orig = head

        while orig:
            copy = Node(orig.val)
            copy.next = orig.next
            orig.next = copy
            orig = orig.next.next
        
        orig = head
        while orig and orig.next:
            orig.next.random = orig.random.next if orig.random else None
            orig = orig.next.next
        
        copy = copy_head = head.next
        
        while copy and copy.next:
            copy.next = copy.next.next
            copy = copy.next
        
        return copy_head