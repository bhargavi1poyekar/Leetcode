class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = None

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
           return -1
        curr = self.head
        for i in range(index):
            curr = curr.next        
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        curr = self.head
        newnode = ListNode(val)
        
        if index <= 0:
            newnode.next = curr
            self.head = newnode
        else:
            for i in range(index-1):
                curr = curr.next
            newnode.next = curr.next
            curr.next = newnode
        
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size: return

        curr = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for i in range(index-1):
                curr = curr.next
            curr.next = curr.next.next
        
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)