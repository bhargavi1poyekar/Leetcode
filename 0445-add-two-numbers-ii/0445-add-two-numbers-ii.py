# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverseLists(head):

            prev=None
            curr=head

            while curr:
                nn=curr.next
                curr.next=prev
                prev=curr
                curr=nn
            
            return prev
        
        l1=reverseLists(l1)
        l2=reverseLists(l2)

        carry=0

        head=curr=ListNode()

        while l1 or l2 or carry:

            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0

            ans=val1+val2+carry

            sum=ans%10
            carry=ans//10

            node=ListNode(sum)

            curr.next=node
            curr=curr.next

            l1=l1.next if l1 else 0
            l2=l2.next if l2 else 0
        
        return reverseLists(head.next)


