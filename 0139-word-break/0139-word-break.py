class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        Given -> string s and dictionary of strings. wordDict. 
        Return true if s -> segmented into space separated sequen of one or more(not all) dictionary words. 

        we can use same words -> multiple times. 

        Match: Dynamic programming

        Plan:
        function: -> dp(i) -> i being the current index of the string that we are matching. 
        dp(i) -> return true if that index character can be found in the wordDict words.

        Relation:
        dp(i) -> will be true, when for words in wordDict:
            dp[i - len(word)] -> also true. and s[i - len(word) + 1: i+1] == matches the word.  
        
        Base Case: if i < 0 -> return True.
        '''

        # Implementation:

        def dp(i):
            if i < 0:
                return True

            if i in memo:
                return memo[i]
            
            for word in wordDict:
                if i >= len(word)-1 and dp(i - len(word)):
                    if s[i - len(word) + 1: i+1] == word:
                        memo[i] = True
                        return memo[i]
                
            memo[i] = False
            return memo[i]
        
        memo = {}
        return dp(len(s)-1)

        '''
        Time Complexity: O(n . m. k) -> n states -> for i, m -> number of words, k -> operation for each word. 

        Space Complexity: O(n)
        '''
                
            