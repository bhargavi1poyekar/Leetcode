class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        Understand:

        Given a string s -> 3 types (, ), *
        return true if s is valid. 

        Valid Rules:

        1. left should have right
        2. right must have left before right. 
        3. * can be (, ), empty. 

        Match: We can use stacks to validate. Because for every close bracket -> we need open bracket. Greedy Approach 

        Plan:
        have 2 stacks -> one for open, and one for *. 
        Whenever we get close, we first check if we have open bracket, we pop it. 
        if not, then we check * -> we pop it. 
        if even * is not there -> then not a valid string. 

        Once traversal of s is complete. Now close is balanced. 

        Now to balance the remaining open -> first check if num stack > num open, if not, there are not enough stars to balance open -> return false. 

        Now, we were storing indexes of these brackets, so while check match for open, we need star to have index more than open. 

        if open top > star top -> return False.
        else. Pop both stacks. 

        AT end, return true if open brackets stack is empty.         
        '''

        open_stack = []
        star_stack = []

        for i, char in enumerate(s):
            if char == '(':
                open_stack.append(i)
            elif char == '*':
                star_stack.append(i)
            else:
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        
        if len(star_stack) < len(open_stack):
            return False
        
        while open_stack and star_stack:
            # print(open_stack, star_stack)
            if open_stack[-1] < star_stack[-1]:
                open_stack.pop()
                star_stack.pop()
            else:
                return False
        
        # print(open_stack)
        if not open_stack:
            return True
        # return False

        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''


