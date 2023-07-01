# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        dummy=head.next

        while(head and head.next):

            nextpair=head.next.next
            head.next.next=head
            if nextpair and nextpair.next:
                head.next=nextpair.next
            else:
                head.next=nextpair
            
            head=nextpair
        
        return dummy
            
