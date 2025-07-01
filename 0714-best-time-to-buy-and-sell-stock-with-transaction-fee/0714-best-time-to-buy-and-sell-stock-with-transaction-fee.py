class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        @lru_cache(None)
        def dp(i, holding):
            if i == len(prices):
                return 0
            
            doNothing = dp(i+1, holding)

            if holding:
                doSomething = dp(i+1, False) + prices[i] - fee
            else:
                doSomething = dp(i+1, True) - prices[i]
            
            return max(doNothing, doSomething)
         
        return dp(0, False)