# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        smallHead = s_ptr = ListNode()
        bigHead = b_ptr = ListNode()

        curr = head

        while curr:
            if curr.val < x:
                s_ptr.next = curr
                s_ptr, curr = s_ptr.next, curr.next
            else:
                b_ptr.next = curr
                b_ptr, curr = b_ptr.next, curr.next
        
        s_ptr.next = bigHead.next
        b_ptr.next = None

        return smallHead.next