# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        prev=None
        slow=head
        fast=head
        count=0

        # Find middle of linked list
        while(fast and fast.next):
            prev=slow
            slow=slow.next
            fast=fast.next.next
            count+=2

        curr=slow
        con, tail=prev,curr

        # Reversing the remaining part of linked list.
        while(curr):
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        
        if con:
            con.next=prev
        else:
            head=prev
        
        tail.next=curr

        diff_n=count//2
        slow=head
        fast=head
        max_sum=0
        while(fast):
            if diff_n<1:
                max_sum=max(max_sum,slow.val+fast.val)
                slow=slow.next
            fast=fast.next
            diff_n-=1
        
        return max_sum
        

