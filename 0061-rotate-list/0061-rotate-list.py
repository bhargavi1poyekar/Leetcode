# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        Given -> head
        To Return -> rotated linked list by k places. 

        N => len of LL
        if k == N -> no rotation reqired. 
        if we have no nodes or only one node -> no rotation required. 

        k can be greater than N ? -> Yes

        Match -> Linked List problem. 
        we might use -> normal pointer.

        Plan -> 
        1. Handle edge cases -> empty, length 1 and k == 0 -> no rotation. 
        2. Count the nodes in list. (again after counting) -> check k % n == 0 -> no rotation required. 
        3. While counting, we go to end of list -> we join the last node to first node, and create a cycle. 
        4. Now we have to take our pointer -> n - k - 1 position. 
        5. At that position -> we make its next as head. 
        6. and then we create curr.next == None. 

        1 -> 2 -> 3 -|> 4 -> 5 -> 1
        5 - 2 - 1 = 2
        we make 3.next -> 4 as head.
        '''

        if not head or not head.next or k == 0:
            return head

        count = 1
        curr = head

        while curr and curr.next:
            curr = curr.next
            count += 1
        
        # print(count)
        k = k % count
        if k == 0:
            return head
        
        curr.next = head

        curr = head
        while count - k - 1:
            curr = curr.next
            count -= 1
        
        # print(curr)
        
        head = curr.next
        curr.next = None
        
        return head

        



