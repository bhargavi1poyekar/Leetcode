# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        '''
        Understand:

        Given head of LL. 
        Revere nodes of list k at a time. 

        return modified list. 

        k is pos integer <= length of ll. 
        if num nodes -> not multiple of k -> let them remain as it is. 

        Nodes need to be changed. 

        Match: Reverse ll, count nodes, with con, tail. 

        Plan:

        Since we have to reverse every k -> only if there are k nodes. 
        So first we have to count k nodes. once we know, there are k nodes.

        Then we reverse from curr to k. 

        Then, again we start from k+1th node, to next k nodes. and so on. 

        We will use reverse Linked list 2 approach, with con tail, for reversing. 
        '''

        count = 0
        count_ptr = head
        curr = head
        prev = None

        while count_ptr and count < k:
            # count = 1
            # :
            count += 1
            count_ptr = count_ptr.next

            if count == k:
                con, tail = prev, curr
                while count:
                    nn = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nn
                    count -= 1
                if con:
                    con.next = prev
                else:
                    head = prev
                
                tail.next = curr
                prev = tail
        
        return head
            


