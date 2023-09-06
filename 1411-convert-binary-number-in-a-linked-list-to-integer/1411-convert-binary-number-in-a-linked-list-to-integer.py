# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        # dec=head.val
        # while(head.next):
        #     dec=dec*2+head.next.val
        #     head=head.next
        
        # return dec

        dec=head.val

        while head.next:
            dec=dec*2+head.next.val
            head=head.next
        
        return dec