# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        head=head.next
        slow=head
        fast=head
        sum=0
        while(fast):
            while(fast.val!=0):
                sum+=fast.val
                fast=fast.next
            slow.val=sum
            sum=0
            slow.next=fast.next
            slow=fast.next
            fast=fast.next
        
        return head

