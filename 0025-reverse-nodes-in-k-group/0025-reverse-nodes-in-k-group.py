# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next: return head

        prev=None
        curr=head

        count_ptr=head
        node_count=0

        while(count_ptr):
            while(node_count<k and count_ptr):
                node_count+=1
                count_ptr=count_ptr.next
            # print(count_ptr)
            if node_count==k:
                con,tail=prev,curr
                while(node_count>0):
                    nn=curr.next
                    curr.next=prev
                    prev=curr
                    curr=nn
                    node_count-=1
                
                if con:
                    con.next=prev
                else:
                    head=prev

                tail.next=curr
                prev=tail
                # print(head)

        return head
            




