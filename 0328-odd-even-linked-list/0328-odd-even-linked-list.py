# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Understand

        Given head of ll, grp nodes with odd indices together. 
        follwed by even indices. 

        Return reordered. First is odd, second even. 

        Match: two pointers. 

        Plan:

        o - e - o - e - o
        We put oddhead, and evenhead and first and second position.

        Then make odd.next = even.next -> so it is connected to next odd. 
        and move odd pointer to its next. 

        do the same for even. till the end of list.  
        '''

        if not head or not head.next:
            return head

        odd = oddHead = head
        even = evenHead = head.next

        while odd and odd.next and even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = evenHead
        # even.next = None
        return oddHead
        
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''