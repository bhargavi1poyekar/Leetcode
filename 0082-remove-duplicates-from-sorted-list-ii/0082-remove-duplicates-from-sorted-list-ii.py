# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        prev=dummy
        dummy.next=head

        while head and head.next:
            if head.val!=head.next.val:
                prev=head
                head=head.next
            
            else:
                while head and head.next and head.val==head.next.val:
                    head=head.next
                
                prev.next=head.next
                head=head.next
            
        return dummy.next