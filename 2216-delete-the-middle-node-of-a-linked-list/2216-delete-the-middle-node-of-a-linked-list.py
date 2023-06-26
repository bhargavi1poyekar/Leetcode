# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return None

        # prev=None
        slow=head
        fast=head.next.next

        while(fast and fast.next):

            # prev=slow
            slow=slow.next
            fast=fast.next.next
        
        # if slow:prev.next=slow.next 
        # else: prev.next=None
        if slow.next:
            slow.next=slow.next.next

        return(head)