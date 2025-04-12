# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Understand:

        Given: 2 sorted lists -> list1 and list2. 
        Merge them into 1 sorted list. 

        Can there be duplicates in both lists? -> Yes
        Numbers are > 0 ?
        can the lists be empty -> yes

        Match:
        two pointers -> one for each list

        Plan:
        two pointers. 
        new head.
        till you reach at end of either of list:
            compare the values for both pointers. 
            Join the pointer with lower value to new head
            and increment that pointer. 

        Once you reach the end of one of the list: then just join the remaining list
        '''

        l1 = list1
        l2 = list2

        newhead = h = ListNode()

        while l1 and l2:
            if l1.val <= l2.val:
                h.next = l1
                l1 = l1.next
            else:
                h.next = l2
                l2 = l2.next
            h = h.next
        
        if l1:
            h.next = l1
        
        if l2:
            h.next = l2
        
        return newhead.next

        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''