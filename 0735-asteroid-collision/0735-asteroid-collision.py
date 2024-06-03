class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for ast in asteroids:
            append = True

            while stack and (stack[-1] > 0 and ast < 0):

                if abs(stack[-1]) < abs(ast):
                    stack.pop()
                    continue
                
                elif abs(stack[-1]) == abs(ast):
                    append = False
                    stack.pop()
                
                append = False
                break

            
            if append:
                stack.append(ast)
        
        return(stack)