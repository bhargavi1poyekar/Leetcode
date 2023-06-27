# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        beg=head
        end=head
        
        count=1
        while(count<k):
            beg=beg.next
            count+=1
        
        fast=beg
        while(fast.next):
            fast=fast.next
            end=end.next
        
        beg.val,end.val=end.val,beg.val
        return head
        

        

