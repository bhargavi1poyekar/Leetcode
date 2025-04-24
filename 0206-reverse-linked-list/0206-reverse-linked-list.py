# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Understand:
        given head -> return reverse LL. 
        '''

        curr = head
        prev = None

        while curr:
            nn = curr.next
            curr.next = prev
            prev = curr
            curr = nn
        
        return prev

        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
