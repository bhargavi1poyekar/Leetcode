# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        Understand:

        Given -> head of LL. 
        return if ll has cycle. 

        Match: slow and fast pointer. 

        Plan:
        we start slow and fast from head, but fast at twice speed of slow. 
        slow moves by 1, and fast moves by 2. 

        if both meet -> then there is a cycle. -> return True
        else if exists loop, because, fast becomes None -> then no Cycle. 
        '''

        if not head:
            return False

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
        
        '''
        Time Complexity: O(N)
        Space COmplexity: O(N)
        '''