# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow=head
        fast=head

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        prev=None
        curr=slow

        while curr:
            nn=curr.next
            curr.next=prev
            prev=curr
            curr=nn
        
        max_sum=0

        while head and prev:
            max_sum=max(max_sum,head.val+prev.val)
            head=head.next
            prev=prev.next
        
        return max_sum
