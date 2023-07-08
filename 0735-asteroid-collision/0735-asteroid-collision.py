class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack=[]

        for mag in asteroids:
            flag=True
            while stack and (stack[-1]>0 and mag<0):

                if abs(stack[-1])<abs(mag):
                    stack.pop()
                    continue
                elif abs(stack[-1])==abs(mag):
                    stack.pop()
                    flag=False
                
                flag=False
                break
                
            if flag==True:
                stack.append(mag)
            
        return stack
