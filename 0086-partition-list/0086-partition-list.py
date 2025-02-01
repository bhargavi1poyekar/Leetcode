# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smallhead = small = ListNode()
        bighead = big = ListNode()
        curr = head

        while curr:
            if curr.val < x:
                small.next = curr
                curr = curr.next 
                small = small.next
            else:
                big.next = curr
                curr = curr.next
                big = big.next
        
        small.next = bighead.next
        big.next = None
        return smallhead.next