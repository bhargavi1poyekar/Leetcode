# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k == 0:
            return head

        curr = head
        count = 1

        while curr and curr.next:
            curr = curr.next
            count += 1

        k = k % count

        if k == 0:
            return head
        
        curr.next = head
        
        curr = head
        while count - k > 1:
            curr = curr.next
            count -= 1
        
        head = curr.next
        curr.next = None

        return head
        


