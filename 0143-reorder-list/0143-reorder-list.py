# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        '''
        Go to middle, separate the list, reverse, and then merge. 
        '''
        if not head or not head.next:
            return head

        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        prev = None
        curr = slow

        while curr:
            nn = curr.next
            curr.next = prev
            prev = curr
            curr = nn
        
        newhead = newcurr = ListNode()
        while head and prev:
            newcurr.next = head
            newcurr = newcurr.next
            head = head.next
            newcurr.next = prev
            newcurr = newcurr.next
            prev = prev.next
        
        return newhead.next

        


        