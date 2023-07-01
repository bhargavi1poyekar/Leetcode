# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k==0:
            return head
        
        count=1
        curr=head
        while(curr.next):
            count+=1
            curr=curr.next

        k=k%count
        if k==0:
            return head

        curr.next=head

        prev=None
        curr=head

        n=count
        pos=0
        while(pos<(n-k)):
            prev=curr
            curr=curr.next
            pos+=1

        head=prev.next
        prev.next=None
        return(head)


        
