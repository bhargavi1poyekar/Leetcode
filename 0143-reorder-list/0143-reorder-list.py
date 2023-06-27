# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head.next: return head

        slow=head
        fast=head

        while(fast and fast.next):
            prev=slow
            slow=slow.next
            fast=fast.next.next

        curr=slow
        prev.next=None
        prev=None
       
        while(curr):
            nn=curr.next
            curr.next=prev
            prev=curr
            curr=nn
       
        h=dummy=ListNode()

        while(head and prev):
            dummy.next=head
            dummy,head=dummy.next,head.next
            dummy.next=prev
            dummy,prev=dummy.next,prev.next
        
        return(h.next)

