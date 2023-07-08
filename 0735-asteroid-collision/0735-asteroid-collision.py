class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack=[] 

        for mag in asteroids:
            doAppend=True # Flag to check if curr element survives collision
            while stack and (stack[-1]>0 and mag<0): 
                # while curr element and stack top, moving towards each other
                if abs(stack[-1])<abs(mag): # if curr element greater
                    stack.pop() # top gets destroyed
                    continue # continue to check with next stack top
                elif abs(stack[-1])==abs(mag): # if both are equal, both get destroyed
                    stack.pop() # top is destroyed
                    doAppend=False # and curr is destroyed so not appended
                
                doAppend=False # if top > curr, then curr gets destroyed
                break
                
            if doAppend: # if survived collision, append it.
                stack.append(mag)
            
        return stack
