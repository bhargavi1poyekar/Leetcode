# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        # parts = [[] for i in range(k)]
        parts = []
        
        # Count nodes. 

        curr = head
        num_nodes = 0
        while curr:
            curr = curr.next
            num_nodes += 1

        parts_with_extra_node = num_nodes % k
        num_nodes_in_each_part = num_nodes // k

        curr = head
        for i in range(k):
            newcurr = newhead = ListNode()
            count = 0
            if i < parts_with_extra_node:
                while curr and count < num_nodes_in_each_part + 1:
                    newcurr.next = curr
                    newcurr = newcurr.next
                    curr = curr.next
                    count += 1
            else:
                while curr and count < num_nodes_in_each_part:
                    newcurr.next = curr
                    newcurr = newcurr.next
                    curr = curr.next
                    count += 1
            
            newcurr.next = None
            parts.append(newhead.next)

        return parts