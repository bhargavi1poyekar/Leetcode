# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        if not head or not head.next or k == 0:
            return head

        node_count = 1
        curr = head

        while curr.next:
            curr = curr.next
            node_count += 1
        
        k = k % node_count 
        if k == 0:
            return head
        
        curr.next = head

        curr = head
        
        while node_count - k > 1:
            curr = curr.next
            node_count -= 1
        
        
        head = curr.next
        curr.next = None

        return head 


        