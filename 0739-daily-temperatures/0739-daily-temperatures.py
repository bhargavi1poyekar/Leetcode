class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack=[]
        answer=[0 for i in range(len(temperatures))]

        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                j=stack.pop()
                answer[j]=i-j
            
            stack.append(i)
        
        return answer