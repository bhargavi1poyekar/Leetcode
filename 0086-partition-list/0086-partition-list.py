# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        small = shead = ListNode()
        big = bhead = ListNode()

        curr = head

        while curr:
            if curr.val < x:
                small.next = curr
                small, curr = small.next, curr.next
            else:
                big.next = curr
                big, curr = big.next, curr.next
        
        small.next = bhead.next
        big.next = None
    
        return shead.next

        

                