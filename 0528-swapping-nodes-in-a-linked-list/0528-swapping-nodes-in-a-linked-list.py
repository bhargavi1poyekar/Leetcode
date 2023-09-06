# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        fast=head
        
        while k!=0:
            beg=fast
            fast=fast.next
            k-=1
        
        end=head
        while fast:
            fast=fast.next
            end=end.next
        
        beg.val,end.val=end.val,beg.val

        return head
