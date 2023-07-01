# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        curr=head
        n=0
        # Find length of linked list
        while(curr):
            n+=1
            curr=curr.next
        
        each_part_nodes=n//k
        extra_nodes_part=n%k
        print(each_part_nodes, extra_nodes_part)

        ans=[]
        curr=head
        for i in range(1,k+1):
            h=dummy=ListNode()
            if i<=extra_nodes_part:
                
                for node in range(each_part_nodes+1):
                    h.next=curr
                    h,curr=h.next,curr.next
                h.next=None
            else:
                for node in range(each_part_nodes):
                    h.next=curr
                    h,curr=h.next,curr.next
                h.next=None
            ans.append(dummy.next)
        
        return ans
                











