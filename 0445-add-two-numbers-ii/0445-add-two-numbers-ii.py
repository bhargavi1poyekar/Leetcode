# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1=self.reverseList(l1)
        l2=self.reverseList(l2)

        dummy=ListNode()
        curr=dummy
        carry=0
        while(l1 or l2 or carry):
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0

            val=val1+val2+carry
            carry=val//10
            val=val%10

            newnode=ListNode(val)
            curr.next=newnode
            curr=curr.next

            l1=l1.next if l1 else 0
            l2=l2.next if l2 else 0

        return self.reverseList(dummy.next) 

        
        
    def reverseList(self,head):

        if not head or not head.next:
            return head
        
        prev=None
        curr=head

        while(curr):
            nn=curr.next
            curr.next=prev
            prev=curr
            curr=nn
        
        return prev

