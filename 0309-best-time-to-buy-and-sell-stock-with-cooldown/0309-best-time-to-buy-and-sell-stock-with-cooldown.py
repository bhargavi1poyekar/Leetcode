class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache
        def dp(i, prevDaySold, holding):
            if i == len(prices):
                return 0
            
            doNothing = dp(i+1, False, holding)
            doSomething = 0

            if holding:
                doSomething = prices[i] + dp(i+1, True, 0)
            elif not holding and not prevDaySold:
                doSomething = -prices[i] + dp(i+1, False, 1)
            
            return max(doSomething, doNothing)
        
        return dp(0, False, 0)