class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        @lru_cache
        def dp(i, holding, remainT):
            if i >= len(prices) or remainT == 0:
                return 0
            
            doNothing = dp(i+1, holding, remainT)

            if holding:
                # Sell
                doSomething = dp(i+1, False, remainT-1) + prices[i]
            else:
                # Buy
                doSomething = dp(i+1, True, remainT) - prices[i]
            
            return max(doNothing, doSomething)
        
        return dp(0, False, k)
