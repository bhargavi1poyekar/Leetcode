# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        curr=head
        n=0
        while(curr):
            curr=curr.next
            n+=1
        
        min_nodes_each_part=n//k
        extra_nodes_part=n%k

        ans=[]
        curr=head
       
        for i in range(1,k+1):
            if i<=extra_nodes_part:
                h1=dummy=ListNode()
                for nodes in range(min_nodes_each_part+1):
                    h1.next=curr
                    h1,curr=h1.next,curr.next
                h1.next=None
            else:
                h1=dummy=ListNode()
                for nodes in range(min_nodes_each_part):
                    h1.next=curr
                    h1,curr=h1.next,curr.next
                h1.next=None
            
            ans.append(dummy.next)
        
        return ans

                
                    


        
