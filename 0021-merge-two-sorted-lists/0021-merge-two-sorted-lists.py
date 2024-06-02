# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=newhead=ListNode()

        while list1 and list2:
            if list1.val<=list2.val:
                newhead.next=list1
                newhead,list1=newhead.next,list1.next
            else:
                newhead.next=list2
                newhead,list2=newhead.next,list2.next
        
        if list1:
            newhead.next=list1
        elif list2:
            newhead.next=list2
        
        return dummy.next