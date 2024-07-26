class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:


        stack = []
        # outer_explode = False

        for asteroid in asteroids:
            outer_explode = False
            while stack and (stack[-1] > 0 and asteroid < 0):
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(asteroid):
                    outer_explode = True
                    stack.pop()

                outer_explode = True
                break

            if not outer_explode:
                stack.append(asteroid)

        return(stack)

