# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy=ListNode()
        prev=dummy
        dummy.next=head
        curr=head

        while(n):
            curr=curr.next
            n-=1

        while(curr):
            prev=prev.next
            curr=curr.next


        prev.next=prev.next.next
        return dummy.next

        
        
        
