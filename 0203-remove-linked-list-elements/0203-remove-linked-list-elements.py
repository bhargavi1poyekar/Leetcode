# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        h=dummy=ListNode()

        curr=head

        while curr:
            if curr.val!=val:
                h.next=curr
                h=h.next
                curr=curr.next
            else:
                curr=curr.next

        h.next=None
        
        return(dummy.next)

