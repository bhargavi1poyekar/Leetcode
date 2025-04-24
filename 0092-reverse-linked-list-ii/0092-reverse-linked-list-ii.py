# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        '''
        Understand: Given head, and left and right, left <= right. 

        Reverse -> nodes from left to right. 

        Match: reverse ll. 

        Plan:
        We have to use reverse LL, but with some modification.

        First, we go till left position. 

        Then, previous element to left -> con, and curr element is tail. 

        Once done, then we do normal reverse. Just at end. 

        We need to make, con.next = prev and tail.next = curr. 
        '''

        curr = head
        prev = None
        while curr and left > 1:
            prev = curr
            curr = curr.next
            left -= 1
            right -= 1
        
        con, tail = prev, curr

        while curr and right >= 1:
            nn = curr.next
            curr.next = prev
            prev = curr
            curr = nn
            right -= 1

        if con:
            con.next = prev
        else:
            head = prev

        tail.next = curr

        return head 

        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        

