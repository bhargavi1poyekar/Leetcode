# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        count_ptr = head
        curr = head
        num_nodes = 0
        prev = None

        while count_ptr and num_nodes < k:
            count_ptr = count_ptr.next
            num_nodes += 1
            
            if num_nodes == k:
                con, tail = prev, curr
                while num_nodes:
                    nn = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nn
                    num_nodes -= 1
                
                if con:
                    con.next = prev
                else:
                    head = prev
                
                tail.next = curr
                prev = tail
            
        return head

        

        

