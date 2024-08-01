class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]: 

        stack = []
        

        for ast in asteroids:
            explode = False
            while stack and (stack[-1] > 0 and ast < 0):
                if abs(ast) > abs(stack[-1]):
                    stack.pop()
                    continue
                elif abs(ast) == abs(stack[-1]):
                    stack.pop()
                    explode = True
                
                explode = True
                break
            
            if not explode:
                stack.append(ast)
        
        return stack

                



