# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = fast = head
        firstend = None
        while fast and fast.next:
            firstend = slow
            slow = slow.next
            fast = fast.next.next
        
        # firstend.next = None
        prev = None

        curr = slow
        while curr:
            nn = curr.next
            curr.next = prev
            prev = curr
            curr = nn
        
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        
        return True