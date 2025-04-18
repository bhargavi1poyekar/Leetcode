class MinStack:

    '''
    Understand: Designing a stack -> supports push, pop, top and retriev min element. 

    O(1) time complexity for each function

    Match: Stack

    Plan: Keep 2 stacks -> one for normal elements, and other for storing min values at each step. 
    '''

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            min_val = self.min_stack[-1]
            if min_val > val:
                self.min_stack.append(val)
            else:
                self.min_stack.append(min_val)
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop()

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