# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        newhead = newcurr = ListNode()

        curr = head.next
        sum_merge = 0

        while curr:
            if curr.val != 0:
                sum_merge += curr.val
            else:
                newcurr.next = ListNode(sum_merge)
                newcurr = newcurr.next
                sum_merge = 0
            curr = curr.next
        
        return newhead.next
        
