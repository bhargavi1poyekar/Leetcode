class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        if len(popped) != len(pushed):
            return False

        pop_idx = 0
        stack = []
        pop_len = len(popped)

        for ch in pushed:
            stack.append(ch)
            while stack  and stack[-1] == popped[pop_idx]:
                stack.pop()
                pop_idx += 1
            
        while stack and stack[-1] == popped[pop_idx]:
                stack.pop()
                pop_idx += 1
            
        return not len(stack) and pop_idx == pop_len