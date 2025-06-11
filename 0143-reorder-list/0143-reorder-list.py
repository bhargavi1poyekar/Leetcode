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
        
        curr = nHead = ListNode()

        while head and head2:
            curr.next = head
            curr, head = curr.next, head.next
            curr.next = head2
            curr, head2 = curr.next, head2.next
        
        return nHead.next



        
        
