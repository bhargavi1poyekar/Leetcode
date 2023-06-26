# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        
        if not head:
            return head
            
        count=1
        ptr=head
        while(ptr.next):
            ptr=ptr.next
            count+=1

        k=k%count
        # print(count,k)
        ptr.next=head
        new_end=count-k
        ptr=head
        # print(new_end)

        while(new_end>1):
            ptr=ptr.next
            new_end-=1

        head=ptr.next
        ptr.next=None
        
        return head


        # if not head or k==0:
        #     return head
        # count=0
        # ptr=head
        # while(ptr):
        #     ptr=ptr.next
        #     count+=1
        # print(count)
        # # print(count)
        # k=k%count
        # if count==1 or k==0:
        #     return head
        # head=self.reverseList(head,1,count)
        # head=self.reverseList(head,1,k)
        # head=self.reverseList(head,k+1,count)
        # return head
    
    # def reverseList(self,head,left,right):

    #     if not head or left==right :
    #         return head
        
    #     prev=None
    #     curr=head

    #     while(left>1):
    #         prev=curr
    #         curr=curr.next
    #         left,right=left-1,right-1

    #     con,tail=prev,curr
    #     while(right and curr):
    #         nn=curr.next
    #         curr.next=prev
    #         prev=curr
    #         curr=nn
    #         right-=1
        
    #     if con:
    #         con.next=prev
    #     else:
    #         head=prev
        
    #     tail.next=curr
    #     return head


        