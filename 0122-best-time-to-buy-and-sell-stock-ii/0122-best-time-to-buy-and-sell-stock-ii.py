class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache
        def dp(i, holding):
            if i == len(prices):
                return 0
            
            doNothing = dp(i+1, holding)
            doSomething = 0

            if holding:
                doSomething = prices[i] + dp(i+1, 0)
            else:
                doSomething = -prices[i] + dp(i+1, 1)
            
            return max(doSomething, doNothing)
        
        return dp(0, 0)