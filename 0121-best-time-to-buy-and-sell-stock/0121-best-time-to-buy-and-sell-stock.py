class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache()
        def dp(i, remaining, holding):
            if i == len(prices) or remaining == 0:
                return 0
            
            # doSomething = 0
            doNothing = dp(i+1, remaining, holding)

            if holding:
                doSomething = dp(i+1, remaining - 1, False) + prices[i]
            else:
                doSomething = dp(i+1, remaining, True) - prices[i]
            
            return max(doNothing, doSomething)
        
        return dp(0, 1, False)
