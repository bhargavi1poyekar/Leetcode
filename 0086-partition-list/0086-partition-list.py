# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        small = shead = ListNode()
        great = ghead = ListNode()
        curr = head

        while curr:
            if curr.val < x:
                small.next = curr
                curr, small = curr.next, small.next
            else:
                great.next = curr
                curr, great = curr.next, great.next
        
        small.next = ghead.next
        great.next = None
    
        return shead.next

