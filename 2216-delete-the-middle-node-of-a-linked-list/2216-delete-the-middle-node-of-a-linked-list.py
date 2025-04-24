# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Understand:

        Given head of LL. 
        Delete the middle node and return head of modified list. 

        Match: Slow and fast. 
        Plan:

        We need slow, fast and prev pointer. 
        while fast reaches end, slow reached middle. 
        Now prev should be one node before slow. 

        So that we can skip slow.
        '''

        if not head or not head.next:
            return None

        slow = fast = head

        prev = dummy = ListNode()
        dummy.next = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = slow.next
        return dummy.next

        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
