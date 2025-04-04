class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)

        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        gas_curr = 0

        for i in range(n):
            gas_curr += gas[i] - cost[i]

            if gas_curr < 0:
                gas_curr = 0
                start = i + 1
        
        return start
