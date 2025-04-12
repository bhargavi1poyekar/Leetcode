class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        Understand:

        string with Digits -> 2 - 9
        Return letter combinations that number could represent. 

        Match:
        Combinations -> backtracking. 

        Plan:

        Hash -> digits with letters. 

        send index, and current combination as parameters. 
        if index == len(digits):
            append combination to answers. 

        traverse over hash of curr digit
        add it to the curr, call backtrack, and remove from curr. 
        '''
        if not digits:
            return []

        def backtrack(curr, i):
            if i == len(digits):
                ans.append(''.join(curr))
                return 
            
            for letter in hash[digits[i]]:
                curr.append(letter)
                backtrack(curr, i+1)
                curr.pop()
        
        ans = []
        hash = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        backtrack([], 0)
        return ans
