# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head and not head.next:
            return head

        beg = head

        while k > 1:
            beg = beg.next
            k -= 1
        
        end = head
        fast = beg

        while fast and fast.next:
            fast = fast.next
            end = end.next
        
        beg.val, end.val = end.val, beg.val
        return head