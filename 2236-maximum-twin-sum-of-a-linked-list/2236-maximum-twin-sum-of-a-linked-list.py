# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None

        curr = slow
        prev = None

        while curr:
            nn = curr.next
            curr.next = prev
            prev = curr
            curr = nn
        
        head2 = prev

        max_twin_sum = 0

        while head and head2:
            twin_sum = head.val + head2.val
            max_twin_sum = max(twin_sum, max_twin_sum)
            head, head2 = head.next, head2.next
        
        return max_twin_sum



        
        