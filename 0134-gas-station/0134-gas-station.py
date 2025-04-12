class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(cost) > sum(gas):
            return -1

        start_index = 0
        curr_gas = 0
        
        for i in range(len(gas)):
            curr_gas += gas[i] - cost[i]
            if curr_gas < 0:
                curr_gas = 0 
                start_index = i + 1
        
        return start_index