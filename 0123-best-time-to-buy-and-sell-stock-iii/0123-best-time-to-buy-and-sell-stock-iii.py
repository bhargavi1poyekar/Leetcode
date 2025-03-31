class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache
        def dp(i, remainingTrans, holding):
            if i == len(prices) or remainingTrans == 0:
                return 0
            
            doNothing = dp(i+1, remainingTrans, holding)
            doSomething = 0

            if holding:
                doSomething = prices[i] + dp(i+1, remainingTrans-1, 0)
            else:
                doSomething = -prices[i] + dp(i+1, remainingTrans, 1)
            
            return max(doSomething, doNothing)
        
        return dp(0, 2, 0)