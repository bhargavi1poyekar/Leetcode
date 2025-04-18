class Solution:
    def numDecodings(self, s: str) -> int:
        
        def dp(i):
            if i == len(s):
                return 1
            
            if s[i] == '0':
                return 0
            
            if i == len(s)-1:
                return 1
            
            if i not in memo:
                ways = dp(i+1)
                if int(s[i:i+2]) <= 26:
                    ways += dp(i+2)
                
                memo[i] = ways
            
            return memo[i]

        
        memo = {}
        return dp(0)
        
