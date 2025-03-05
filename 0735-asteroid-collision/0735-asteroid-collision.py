class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for ast in asteroids:
            # print(stack)
            explode = False
            while stack and (ast < 0 and stack[-1] > 0):
                # print(stack, ast)
                if stack[-1] > abs(ast):
                    explode = True
                    break
                elif stack[-1] == abs(ast):
                    stack.pop()
                    explode = True
                    break
                elif stack[-1] < abs(ast):
                    stack.pop()
                    # explode = False
            
            if explode == False:
                stack.append(ast)
        
        return stack

                
