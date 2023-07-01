# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        grp=2
        node_count=0
        count_ptr=head.next
        curr=head.next
        prev=head

        while(curr):
            while(count_ptr and node_count<grp):
                count_ptr=count_ptr.next
                node_count+=1
            print(node_count)
            
            if node_count%2==0:
                con,tail=prev,curr
                while(node_count and curr):
                    nn=curr.next
                    curr.next=prev
                    prev=curr
                    curr=nn
                    node_count-=1
                
                con.next=prev
                tail.next=curr
                prev=tail
            
            else:
                curr=count_ptr
                while(prev.next!=curr):
                    prev=prev.next
                    
            node_count=0
            grp+=1
        
        return head




