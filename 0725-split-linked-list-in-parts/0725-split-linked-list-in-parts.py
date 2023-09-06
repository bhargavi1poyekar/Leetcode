# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        curr=head
        num_nodes=0

        while curr:
            num_nodes+=1
            curr=curr.next
        
        num_parts=num_nodes//k
        parts_with_extra=num_nodes%k

        parts=[]
        curr=head
        for i in range(k):
            h=dummy=ListNode()
            count=0
            if i<parts_with_extra:
                while curr and count<num_parts+1:
                    h.next=curr
                    h=h.next
                    curr=curr.next
                    count+=1
               
            else:
                while curr and count<num_parts:
                    h.next=curr
                    h=h.next
                    curr=curr.next
                    count+=1
                    
            h.next=None
            parts.append(dummy.next)
        
        return parts