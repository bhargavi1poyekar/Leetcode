class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(remaining_amt):
            # print(remaining_amt)
            if remaining_amt < 0:
                return -1
            if remaining_amt == 0:
                return 0

            if remaining_amt not in memo:
                min_coins = float('inf')
                for coin in coins:
                    result = dfs(remaining_amt - coin)
                    if result != -1:
                        min_coins = min(min_coins, result + 1)
                memo[remaining_amt] = min_coins if min_coins != float('inf') else -1
            
            return memo[remaining_amt]

        memo = {}
        return dfs(amount)