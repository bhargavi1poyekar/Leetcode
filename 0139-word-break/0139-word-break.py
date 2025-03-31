class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def dp(i):
            if i < 0: 
                return True
            if i in memo:
                return memo[i]
            
            for word in wordDict:
                if (i >= len(word) - 1) and dp(i - len(word)):
                    if s[i - len(word) + 1 : i + 1] == word:
                        memo[i] = True
                        return memo[i]
            
            memo[i] = False
            return memo[i]
        
        memo = {}
        return dp(len(s) - 1)