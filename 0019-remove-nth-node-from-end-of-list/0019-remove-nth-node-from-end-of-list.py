# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        '''
        Understand:

        Given -> head of linked list. 
        Remove -> nth node from end of list. 
        Return head. 

        Match:
        slow and fast pointer.

        Plan:
        we have slow and fast at head. 

        We also create dummy senteniel node -> since nth node cna be head as well. 

        Then we first start fast -> and keep a gap of n elements between fast and slow. So when fast reached end. slow reaches at nth node from end. 

        we also keep a prev node behind slow. So once slow reaches at nth node from end. we can connect prev with the next of slow. 
        '''

        prev = dummy = ListNode()
        dummy.next = head
        slow = fast = head

        while n and fast:
            fast = fast.next
            n -= 1
        
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        prev.next = slow.next
        return dummy.next

        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''

        
