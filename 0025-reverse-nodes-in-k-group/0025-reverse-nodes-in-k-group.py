# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head and not head.next:
            return head

        count = 0
        curr = count_ptr = head
        prev = None

        while count_ptr and count < k:
            count_ptr = count_ptr.next
            count += 1

            if count == k:
                con = prev
                tail = curr

                while count:
                    nn = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nn
                    count -= 1

                if not con:
                    head = prev
                else:
                    con.next = prev
                tail.next = curr
                prev = tail
            
        return head

                
