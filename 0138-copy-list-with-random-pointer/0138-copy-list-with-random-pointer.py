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
            return head
        
        curr = head

        while curr:
            newnode = Node(curr.val)
            newnode.next = curr.next
            curr.next = newnode
            curr = curr.next.next
        
        orig = head

        while orig:
            orig.next.random = orig.random.next if orig.random else None
            orig = orig.next.next
        
        copyHead = copy = head.next

        while copy and copy.next:
            copy.next = copy.next.next
            copy = copy.next
        
        return copyHead


        