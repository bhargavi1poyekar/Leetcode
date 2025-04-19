class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Understand: 

        Given arr prices -> price on ith day. 

        find max profit -> complete atmost 2 transactions. 

        transactions -> buy and sell. 

        Match: Dynamic Programming. Current decision based on prev decisions. 

        Plan:

        dp(i, holding, remainTrans) -> return max profit that can be achieved on ith day. 

        i -> curr day. 
        holding -> whether we have buyed a stock and holding it. or not. -> boolean. 
        remainTrans -> remaining Transactions. 

        Recurrence Relations:

        On each day -> we can either choose to buy/sell or not do anything and just move to next day. 

        So dp = max(doNothing, doSomething)

        Now for doing something -> it depends on whether we are currently holding a stock, or not. 
        If holding, we can sell.
        if not holding, we can buy. 

        if sell -> go to next day with, dp(i+1, False, remainTrans - 1) + prices[i] (profit)
        if buy -> go to next day with, dp(i+1, True, remainTrans) - prices[i]

        Base Condition:
        if we reached last day, or possible num of transactions completed -> then return 0. 
        '''

        @lru_cache()
        def dp(i, holding, remainTrans):
            if i == len(prices) or remainTrans == 0:
                return 0
            
            doNothing = dp(i+1, holding, remainTrans)

            if holding:
                # sell
                doSomething = dp(i+1, False, remainTrans - 1) + prices[i]
            else:
                doSomething = dp(i+1, True, remainTrans) - prices[i]
            
            return max(doNothing, doSomething)

        return dp(0, False, 2)

        '''
        Time Complexity: O(n) -> number of states -> n x 2(True/False) x k(here value of k=2) * constant work. 
        Space Complexity: O(n)
        '''

