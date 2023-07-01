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

        if not head or not head.next:
            return head

        slow,fast=head,head
        
        while(fast and fast.next):
            prev=slow
            slow=slow.next
            fast=fast.next.next
        
        prev.next=None

        prev=None
        curr=slow
        while(curr):
            nn=curr.next
            curr.next=prev
            prev=curr
            curr=nn
        
        dummy=ListNode()
        curr=dummy
        
        while(prev and head):
            curr.next=head
            curr,head=curr.next,head.next
            curr.next=prev
            curr,prev=curr.next,prev.next
        
        return dummy.next






