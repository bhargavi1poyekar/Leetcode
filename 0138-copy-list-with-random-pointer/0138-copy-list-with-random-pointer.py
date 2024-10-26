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
            node = ListNode(curr.val)
            node.next = curr.next
            curr.next = node
            curr = curr.next.next

        curr = head
        while curr and curr.next:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next
        
        copyHead = curr = head.next

        while curr and curr.next:
            curr.next = curr.next.next
            curr = curr.next
        return copyHead

        