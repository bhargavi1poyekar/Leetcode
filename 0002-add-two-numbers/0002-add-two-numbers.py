# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        Understand:

        Given -> 2 non empty ll. -> non negative integers. 
        digits stored in reverse order. each node -> single digit. 

        Return -> add 2 numbers -> return as linked list -> reverse order. 

        no leading zeros in list. and only single digits. 

        Match: -> we need 2 pointer -> one for each linked list. 
        And simultaneuosly one for the new Linked list -> that will store the sum.

        Plan:

        we iterate over both lists, till everyone reaches end. 
        and we also need to store any carry during the sum. And check that as well while iterating. 

        Then get the digits from both the linked list and do sum. 
        Now carry would be sum // 10 and the remainder will be storeed in the new node. 

        We create new node -> store the remainder in it. and then move all the pointers forward. We do this till both lists are covered, and there is no carry. 
        '''

        h = newhead = ListNode()
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            add = val1 + val2 + carry
            carry = add // 10
            rem = add % 10

            # print(rem)

            newnode = ListNode(rem)
            h.next = newnode

            h = h.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return newhead.next

