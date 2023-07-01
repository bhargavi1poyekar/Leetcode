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
        
        each_part_nodes=n//k # Min nodes in each part
        extra_nodes_part=n%k # Number of parts with extra nodes
       

        ans=[]
        curr=head
        for i in range(1,k+1): # For every part
            h=dummy=ListNode() # Create an empty list
            if i<=extra_nodes_part: # Parts with extra node
                for node in range(each_part_nodes+1):
                    h.next=curr 
                    h,curr=h.next,curr.next
                h.next=None
            else:
                for node in range(each_part_nodes): # Parts with min nodes.
                    h.next=curr
                    h,curr=h.next,curr.next
                h.next=None

            ans.append(dummy.next) # Append list to part 
        
        return ans
                











