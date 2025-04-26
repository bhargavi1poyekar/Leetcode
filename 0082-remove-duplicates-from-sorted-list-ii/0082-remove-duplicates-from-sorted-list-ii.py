# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Understand:

        Given head of sorted ll. 

        delete all nodes that have duplicates. leaving only distinct numbers. 

        list should be sorted. 

        Match: 2 pointers, and dummy node. 

        Plan:

        We start traversing. With dummy and prev. 

        Now we check for curr and curr.next -> if not same, then we move curr forward, as well as prev. 

        But if they are same, while curr and curr.next is same, we will continue just moving forward curr. once curr not equa to curr.next. we skip all the inbetween nodes, and connect prev.next = curr. 

        but again we need to check, if the curr and its next are same. Only if they are diff. we will move prev = prev.next. 
        '''

        prev = dummy = ListNode()
        dummy.next = head

        curr = head

        while curr and curr.next:
            if curr.val != curr.next.val:
                prev = prev.next
                curr = curr.next
            else:
                while curr and curr.next and curr.val == curr.next.val:
                    curr = curr.next          
                prev.next = curr.next
                curr = curr.next
        
        return dummy.next
            
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        

        
        



