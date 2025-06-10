# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = h1 = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                h1.next = list1
                h1, list1 = h1.next, list1.next
            else:
                h1.next = list2
                h1, list2 = h1.next, list2.next
        
        if list1:
            h1.next = list1
        elif list2:
            h1.next = list2
        
        return head.next

        