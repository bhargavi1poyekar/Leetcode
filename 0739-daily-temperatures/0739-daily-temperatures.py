class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack=[]
        warmer_idx=[0]*len(temperatures) 
        for i in range(len(temperatures)):
            
            while stack and temperatures[stack[-1]]<temperatures[i]:
                idx=stack.pop()
                warmer_idx[idx]=i-idx
            
            stack.append(i)
        
        return warmer_idx

        