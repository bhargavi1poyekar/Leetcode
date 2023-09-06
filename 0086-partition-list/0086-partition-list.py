# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        small=h1=ListNode()
        big=h2=ListNode()

        while head:
            if head.val<x:
                small.next=head
                small,head=small.next,head.next
            else:
                big.next=head
                big,head=big.next,head.next
            
        small.next=h2.next
        big.next=None
        
        return h1.next
