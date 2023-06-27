# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        curr=head
        node_count=0
        while(curr):
            curr=curr.next
            node_count+=1
        
        each_part_count=node_count//k
        node_with_extra=node_count%k

        ans=[]
        for i in range(1,k+1):
            h=curr=ListNode()
            prev=None
            count=0

            if i<=node_with_extra:
                while(count<each_part_count+1):
                    prev=curr
                    curr.next=head
                    curr,head=curr.next,head.next
                    count+=1
                prev.next.next=None
            else:
               
                while(count<each_part_count):
                    prev=curr
                    curr.next=head
                    curr,head=curr.next,head.next
                    count+=1
                if prev: prev.next.next=None
               
            ans.append(h.next)
            count=0
        return ans

                
        
