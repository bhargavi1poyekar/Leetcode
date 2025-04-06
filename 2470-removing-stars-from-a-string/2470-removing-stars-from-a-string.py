class Solution:
    def removeStars(self, s: str) -> str:
        
        '''
        Understand:

        Given -> a string with stars. 
        Operation:
            choose a star -> remove closest non star char to its left, and remove star

        return after all stars removed. 

        Questions: other chars can be anything -> along with * ? yes
        If there is no non star char on left -> remove only the star
        Only stars -> return empty
        No stars -> return orig

        Match: Use stack -> to keep track of non star chars. 

        Plan:
        if non star char -> push into stack. 
        if star: -> if stack -> pop

        return the string of stack at end. 
        '''

        # Implement

        stack = []

        for ch in s:
            if ch != '*':
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
        
        return ''.join(stack)

        '''
        s = 'leet**cod*e'
        stack = [l, e, c, o, e] => return 'lecoe'

        ch = e

        Evaluation:

        Time Complexity -> O(n)
        Space Complexity -> O(n)
        '''
