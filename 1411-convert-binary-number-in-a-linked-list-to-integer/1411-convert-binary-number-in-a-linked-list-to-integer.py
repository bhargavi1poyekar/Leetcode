# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        # ptr=head
        # n=0
        # while(ptr):
        #     ptr=ptr.next
        #     n+=1

        # ptr=head
        # dec=0
        # while(ptr):
        #     if ptr.val==1:
        #         dec+=2**(n-1)
            
        #     n-=1
        #     ptr=ptr.next
        
        # return(dec)

        dec=head.val
        while(head.next):
            dec=dec*2+head.next.val
            head=head.next
        
        return dec
