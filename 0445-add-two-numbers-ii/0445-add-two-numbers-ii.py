# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverseList(head):

            curr = head
            prev = None
            while curr:
                nn = curr.next
                curr.next = prev
                prev = curr
                curr = nn
            return prev

        l1_reverse = reverseList(l1)
        l2_reverse = reverseList(l2)

        carry = 0
        newlist = newhead = ListNode()
        while l1_reverse or l2_reverse or carry:
            num1 = l1_reverse.val if l1_reverse else 0
            num2 = l2_reverse.val if l2_reverse else 0

            sum = num1 + num2 + carry
            carry = sum // 10
            rem = sum % 10 

            newnode = ListNode(rem)
            newlist.next = newnode

            newlist = newlist.next

            l1_reverse = l1_reverse.next if l1_reverse else None
            l2_reverse = l2_reverse.next if l2_reverse else None
        
        return reverseList(newhead.next)

        

        