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

            next_n=head.next.next
            head.next.next=head

            if next_n and next_n.next:
                head.next=next_n.next
            else:
                head.next=next_n
            head=next_n
        
        return dummy