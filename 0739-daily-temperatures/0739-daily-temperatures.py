class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack_index=[]
        future_day=[0 for i in range(len(temperatures))]

        for i in range(len(temperatures)):

            while(stack_index and temperatures[stack_index[-1]]<temperatures[i]):
                idx=stack_index.pop()
                future_day[idx]=i-idx
            
            stack_index.append(i)
        
        return(future_day)