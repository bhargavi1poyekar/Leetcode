# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        '''
        Understand: 
        Given head of LL and val x
        partition such that all nodes less than x -> come before nodes greater or equal to x. 

        Can the list be empty -> Yes
        Can the list have duplicate values -> Yes
        Can the list have negative integers -> Yes

        Match: 2 pointers. one to start linking all nodes less than x 
        and other to start linking all nodes greater/equal to x. 

        Plan:
        we traverse the list. 
        we have 2 pointers. small, and large. 
        So all nodes smaller to x -> attached to small, 
        and nodes larger/equal to x -> attached to large. 

        AT the end -> we join small linked list with larger linked list. 
        '''

        shead = small = ListNode()
        lhead = large = ListNode()
        curr = head

        while curr:
            if curr.val >= x:
                large.next = curr
                large = large.next
            else:
                small.next = curr
                small = small.next
            curr = curr.next
        
        small.next = lhead.next
        large.next = None # this is important. 
        return shead.next

        '''
        Time Complexity -> O(N)
        Space COmplexity -> O(1)
        '''
