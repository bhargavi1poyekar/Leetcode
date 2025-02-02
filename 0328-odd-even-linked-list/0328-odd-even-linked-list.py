# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        oddcurr = head
        evenhead = evencurr = head.next

        while oddcurr and evencurr and oddcurr.next and evencurr.next:
            oddcurr.next = evencurr.next
            oddcurr = oddcurr.next
            evencurr.next = oddcurr.next
            evencurr = evencurr.next
        
        oddcurr.next = evenhead
        # evencurr.next = None
        
        return head

        