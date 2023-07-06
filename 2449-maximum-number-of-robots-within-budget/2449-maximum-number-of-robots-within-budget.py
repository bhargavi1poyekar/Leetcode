class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:

        left=0
        max_charge=deque()
        sum_run=0
        max_length=0

        for right in range(len(chargeTimes)):
            
            while max_charge and max_charge[-1]<chargeTimes[right]:
                max_charge.pop()
                
            max_charge.append(chargeTimes[right])

            sum_run+=runningCosts[right]
            
            while(max_charge and (max_charge[0]+(right-left+1)*sum_run)>budget):
                sum_run-=runningCosts[left]
                if max_charge[0]==chargeTimes[left]:
                    max_charge.popleft()
                left+=1
            
            max_length=max(max_length,right-left+1)
        
        return max_length






