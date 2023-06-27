# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        if not head:return head
        count=n

        dummy=ListNode()
        dummy.next=head

        prev=dummy
        slow,fast=head,head

        while(count>0):
            fast=fast.next
            count-=1
        
        while fast:
            prev=slow
            slow=slow.next
            fast=fast.next

        prev.next=prev.next.next

        return dummy.next
