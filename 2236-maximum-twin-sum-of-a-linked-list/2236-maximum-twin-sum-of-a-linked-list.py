# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # Middle, reverse and add 
        
        prev = None
        slow = head
        fast = head

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

        max_sum = 0
        curr_sum = 0
        while head and prev:
            curr_sum = head.val + prev.val
            head, prev = head.next, prev.next
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
        
        

