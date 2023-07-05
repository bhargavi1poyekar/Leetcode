class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        stack=[]
        pop_idx=0
        for i in pushed:
            stack.append(i)
            while(stack and stack[-1]==popped[pop_idx]):
                stack.pop()
                pop_idx+=1
            
        return not stack
