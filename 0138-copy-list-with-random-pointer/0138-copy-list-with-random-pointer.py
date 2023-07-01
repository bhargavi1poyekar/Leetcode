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

        curr=head
        while(curr):
            copy=Node(curr.val)
            copy.next=curr.next
            curr.next=copy
            curr=curr.next.next
        
        curr=head
        while(curr):
            curr.next.random=curr.random.next if curr.random else None
            curr=curr.next.next
        
        ptr=copyhead=head.next
        while(copyhead and copyhead.next):
            copyhead.next=copyhead.next.next
            copyhead=copyhead.next
        return ptr

        

