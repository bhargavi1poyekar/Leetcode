# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        head=head.next
        start,curr=head,head

        while(curr):
            sum=0
            while(curr.val!=0):
                sum+=curr.val
                curr=curr.next
            start.val=sum
            start.next=curr.next
            curr=curr.next
            start=curr
        
        return head

