class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(i, remainT, holding):
            if i == len(prices) or remainT == 0:
                return 0
            
            doNothing = dp(i+1, remainT, holding)

            if holding:
                doSomething = dp(i+1, remainT-1, False) + prices[i]
            else:
                doSomething = dp(i+1, remainT, True) - prices[i]
            
            return max(doNothing, doSomething)
        
        return dp(0, 2, False)