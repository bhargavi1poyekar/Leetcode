class MyStack:

    def __init__(self):
        self.queue=deque()
        self.queue2=deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        
    def pop(self) -> int:
        while len(self.queue)>1:
            top=self.queue.popleft()
            self.queue2.append(top)
        
        top=self.queue.popleft()
        self.queue2,self.queue=self.queue,self.queue2
        return top

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return not self.queue and not self.queue2


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()