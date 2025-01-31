# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        newlist = newhead = ListNode()

        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            sum = num1 + num2 + carry
            carry = sum // 10
            rem = sum % 10

            new_node = ListNode(rem)
            newlist.next = new_node

            newlist = newlist.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return newhead.next
        