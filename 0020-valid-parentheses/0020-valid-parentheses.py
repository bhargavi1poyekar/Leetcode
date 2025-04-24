class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Understand:

        Given string -> s with chars -> ()[]{}

        return if string is valid. 

        Match: Stack -> so that we can check what we encountered before. 
        And we need to close the latest encounterd open bracket first. LIFO. 

        Plan: 

        we maintain hash -> matching brackets. 
        if we encounter open bracket -> we add its matching close bracket to the stack. 
        Now, when we encounter a close bracket, we check if we have same at the stack top. if no, then not valid. 

        if yes, then we remove the stack top. 
        '''

        match_bracket = {
                            '(':')',
                            '{':'}',
                            '[':']'
                        }
        stack = []
        for ch in s:
            if ch in match_bracket:
                stack.append(match_bracket[ch])
            else:
                if stack and stack[-1] == ch:
                    stack.pop()
                else:
                    return False
        
        return True if not len(stack) else False

        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''

