class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
       
    def push(self, val: int) -> None:
       
        if self.min_stack:
            curr_min = self.min_stack[-1] 
            if val < curr_min:
                self.min_stack.append(val)
            else:
                self.min_stack.append(curr_min)
        else:
            self.min_stack.append(val)
        self.stack.append(val)
        


    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()