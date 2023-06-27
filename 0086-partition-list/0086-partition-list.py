# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        h1=small=ListNode()
        h2=large=ListNode()

        while(head):

            if head.val<x:
                
                small.next=head
                small=small.next

            else:
                
                large.next=head
                large=large.next
            
            head=head.next
        
        large.next=None
        small.next=h2.next

        return h1.next
