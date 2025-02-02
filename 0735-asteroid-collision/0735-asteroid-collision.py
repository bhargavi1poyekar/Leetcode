class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for ast in asteroids:
            explode = False
            while stack and (stack[-1] > 0 and ast < 0):
                if abs(ast) < stack[-1]:
                    explode = True
                    break
                elif abs(ast) == stack[-1]:
                    explode = True
                    stack.pop()
                    break
                else: 
                    stack.pop()
                    # continue
            
            if not explode:
                stack.append(ast)

        return stack 
