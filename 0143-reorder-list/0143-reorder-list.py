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
            
        slow=head
        fast=head
        
        
        while fast and fast.next:
            prev=slow
            fast=fast.next.next
            slow=slow.next
        
        prev.next=None
       
        prev=None
        curr=slow

        while curr:
            nn=curr.next
            curr.next=prev
            prev=curr
            curr=nn
        
        h=dummy=ListNode()
        while prev and head:
            h.next=head
            h,head=h.next,head.next
            h.next=prev
            h,prev=h.next,prev.next
        
        
        return dummy.next
