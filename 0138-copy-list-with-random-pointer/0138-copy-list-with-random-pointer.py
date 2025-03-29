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

        '''Psedocode/ Plan
        7 -> 7`-> 13 -> 13` -> 11 -> 11` -> 10 -> 10` -> 1 -> 1`

        7 
        deep_copy(7) -> create new node with val 7. 
        copy.next = orig.next
        orig.next = copy
        orig = orig.next.next

        traverse the orig nodes. 
        (orig.next == its copy)
        orig.next.random = orig.random.next if orig.random else None
        orig = orig.next.next

        Remove the orig nodes from the list. 
        we start frop copyHead -> orighead.next
        copy.next = copy.next.next
        copy = copy.next.next
        '''
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
        
        copyHead = head.next
        copy = head.next

        while copy and copy.next:
            copy.next = copy.next.next
            copy = copy.next
        
        return copyHead
        



