class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        answer = [0] * len(temperatures)
        mono_stack = []

        for i in range(len(temperatures)):
            while mono_stack and temperatures[mono_stack[-1]] < temperatures[i]:
                index = mono_stack.pop()
                answer[index] = i - index
            
            mono_stack.append(i)
        
        return answer
