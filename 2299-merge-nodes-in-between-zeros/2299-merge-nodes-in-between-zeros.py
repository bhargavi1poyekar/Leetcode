# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        head=head.next
        curr_sum=0
        slow=head
        fast=head
        while fast:
            while fast.val!=0:
                curr_sum+=fast.val
                fast=fast.next
            
            slow.val=curr_sum
            slow.next=fast.next
            curr_sum=0
            slow=slow.next
            fast=fast.next
            
        return(head)



