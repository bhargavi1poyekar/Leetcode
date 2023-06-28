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

        if not head: return head
        curr=head
        while(curr):
            copynode=Node(curr.val)
            copynode.next=curr.next
            curr.next=copynode
            curr=copynode.next
            
        curr=head
        while(curr):
            if curr.random:
                curr.next.random=curr.random.next
            else:curr.next.random=None
            curr=curr.next.next
        
       
        head2=head.next
        # print(head2.val,head2.next,head2.random)
        ptr=head2
        while(ptr and ptr.next):
            ptr.next=ptr.next.next 
            ptr=ptr.next
        
        return head2
