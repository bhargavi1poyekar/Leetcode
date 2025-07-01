class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i, prevDaySold, holding):
            if i == len(prices):
                return 0
            
            doNothing = dp(i+1, False, holding)
            doSomething = 0
            if holding:
                doSomething = dp(i+1, True, False) + prices[i]
            elif not holding and not prevDaySold:
                doSomething = dp(i+1, False, True) - prices[i]
            
            return max(doNothing, doSomething)
         
        return dp(0, False, False)