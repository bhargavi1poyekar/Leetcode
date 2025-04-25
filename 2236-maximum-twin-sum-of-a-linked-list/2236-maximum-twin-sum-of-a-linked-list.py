# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        '''
        Understand:
        given a ll -> we need to break it in middle, reverse the second half, and then have twin sum with first hald and second half. 
        
        Match: Middle + reverse + sum
        '''

        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        curr = slow
        prev.next = None
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
            max_twin_sum = max(max_twin_sum, twin_sum)
            head, head2 = head.next, head2.next

        return max_twin_sum 
        
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
            
        