# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        prev=None
        curr=head

        while left>1:
            prev=curr
            curr=curr.next
            left-=1
            right-=1
        
        con=prev
        tail=curr

        while curr and right>0:
            nn=curr.next
            curr.next=prev
            prev=curr
            curr=nn
        
            right-=1
        
        if not con:
            head=prev
        else:
            con.next=prev
        
        tail.next=curr
        return head




