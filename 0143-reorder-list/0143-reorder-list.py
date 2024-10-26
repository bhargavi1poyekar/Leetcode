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

        if not head or not head.next:
            return head
        
        ## Go to middle of LL:
        
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
        
        newHead = dummy = ListNode()

        while head and prev:
            newHead.next = head
            newHead, head = newHead.next, head.next
            newHead.next = prev
            newHead, prev = newHead.next, prev.next
        
        return dummy.next
            

        