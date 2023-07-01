# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        beg=head
        end=head

        while(k>1):
            beg=beg.next
            k-=1
        
        fast=beg
        while(fast.next):
            end=end.next
            fast=fast.next
        
        beg.val,end.val=end.val,beg.val
    
        return head

