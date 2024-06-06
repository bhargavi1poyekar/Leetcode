class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if self.min_stack:
            curr_min = min(self.min_stack[-1], val)
        else:
            curr_min = val

        self.stack.append(val)
        self.min_stack.append(curr_min) 

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]

'''        
min = [-2, -2, -3]
stack =[-2, 0, -3]

[[-2, -2], [0, -2], [-3, -3]]

Plan:

1. initialize a stack 
2. push -> append in 2 arrays -> min, and stack
3. Pop -> remove the top element
4. Top -> check stack[-1]
5. Set min[-1]


'''


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()