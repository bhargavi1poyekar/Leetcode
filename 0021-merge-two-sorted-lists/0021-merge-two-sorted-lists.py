# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = newHead = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1, dummy = list1.next, dummy.next
            else:
                dummy.next = list2
                list2, dummy = list2.next, dummy.next
        
        if list1:
            dummy.next = list1
        elif list2:
            dummy.next = list2
        
        return newHead.next

        