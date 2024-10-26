# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head and not head.next:
            return head

        curr = head
        prev = None
        node_count = 0
        node_ptr = head
        while node_count < k and node_ptr:
            node_ptr = node_ptr.next
            node_count += 1

            if node_count == k:
                con, tail = prev, curr

                while node_count:
                    nn = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nn
                    node_count -= 1
                
                if con:
                    con.next = prev
                else:
                    head = prev
                tail.next = curr
                prev = tail
            
        return head

            

        