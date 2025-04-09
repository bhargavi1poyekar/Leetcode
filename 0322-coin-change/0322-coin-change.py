class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dp(remain_amt):
            if remain_amt < 0:
                return -1
            if remain_amt == 0:
                return 0
            
            if remain_amt not in memo:
                min_coins = float('inf')
                for c in coins:
                    result = dp(remain_amt - c)
                    if result != -1:
                        min_coins = min(min_coins, result + 1)
                memo[remain_amt] = min_coins if min_coins != float('inf') else -1

            return memo[remain_amt]  
        
        memo = {}
        return dp(amount)