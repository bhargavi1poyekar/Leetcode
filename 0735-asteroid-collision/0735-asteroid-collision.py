class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack=[]
        
        for i in range(len(asteroids)):
            flag=1
            while stack and (stack[-1]>0 and asteroids[i]<0):
                if abs(asteroids[i])>abs(stack[-1]):
                    stack.pop()
                    continue
                elif abs(asteroids[i])==abs(stack[-1]):
                    stack.pop()
                    flag=0
                    
                
                flag=0
                break
            
            if flag:
                stack.append(asteroids[i])

        return stack
            
            
        
        print(stack)
