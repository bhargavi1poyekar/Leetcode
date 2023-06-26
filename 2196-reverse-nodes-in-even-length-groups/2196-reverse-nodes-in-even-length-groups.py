# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        prev=head
        curr=head.next

        grp_count=2
        count=0
        count_ptr=head.next
        node_count=0
        while curr:

            while(count_ptr and node_count<grp_count):
                count_ptr=count_ptr.next
                node_count+=1
                
            if node_count%2==0:
                con,tail=prev,curr
                while(count<grp_count and curr):
                    nn=curr.next
                    curr.next=prev
                    prev=curr
                    curr=nn
                    count+=1
                    
                con.next=prev
                tail.next=curr
                prev=tail
                count=0
            
            else:
                curr=count_ptr
                while(prev.next!=curr):
                    prev=prev.next
            node_count=0
            grp_count+=1
            
        
        return(head)
            

