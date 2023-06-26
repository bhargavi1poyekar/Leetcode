# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head:
            return head
        
        if left==right:
            return head
        
        prev=None
        curr=head

        # Bringing prev and curr to their positions: curr=>left and prev=left-1
        while(left>1):
            prev=curr
            curr=curr.next
            left,right=left-1,right-1 # dec left,n
        
        con,tail=prev,curr

        while(right):
            next_n=curr.next
            curr.next=prev
            prev=curr
            curr=next_n
            right-=1

        if con:
            con.next=prev
        else:
            head=prev
        
        tail.next=curr
        return head
        

        
         
        