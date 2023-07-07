class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        stack=[]
        next_popped=0

        for val in pushed:
            stack.append(val)

            while(stack and stack[-1]==popped[next_popped]):
                stack.pop()
                next_popped+=1
            
        return True if not stack else False
