# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return None

        prev=None
        slow=head
        fast=head

        while(fast and fast.next):
            prev=slow
            slow=slow.next
            fast=fast.next.next
        
        
        prev.next=prev.next.next

        return head