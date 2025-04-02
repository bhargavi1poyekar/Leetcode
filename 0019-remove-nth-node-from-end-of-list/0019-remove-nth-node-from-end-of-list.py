# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        slow = fast = head

        while fast and n > 0:
            fast = fast.next
            n -= 1
        
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        prev.next = slow.next
        return dummy.next