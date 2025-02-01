# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head and head.next:
            return None
        
        prev=head
        curr=head.next

        grp=2
        grp_len=0
        grp_ptr=head.next
    
        while curr:
            while grp_ptr and grp_len<grp:
                grp_len+=1
                grp_ptr=grp_ptr.next

            if grp_len%2==0:
                con=prev
                tail=curr
                while grp_len>0:
                    nn=curr.next
                    curr.next=prev
                    prev=curr
                    curr=nn
                    grp_len-=1
                
                con.next=prev
                tail.next=curr
                prev=tail
            
            else:
                curr=grp_ptr
                while(prev.next!=curr):
                    prev=prev.next
            
            grp_len=0
            grp+=1
        
        return head

                 


        