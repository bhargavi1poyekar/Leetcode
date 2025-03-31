class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache
        def dp(i, remaining, holding):
            if i == len(prices) or remaining == 0:
                return 0
            
            doNothing = dp(i+1, remaining, holding)
            doSomething = 0

            if holding:
                doSomething = prices[i] + dp(i+1, remaining - 1, 0)
            else:
                doSomething = -prices[i] + dp(i+1, remaining, 1)
            
            # print(doSomething, doNothing)
            return max(doSomething, doNothing)
        
        return dp(0, 1, 0)