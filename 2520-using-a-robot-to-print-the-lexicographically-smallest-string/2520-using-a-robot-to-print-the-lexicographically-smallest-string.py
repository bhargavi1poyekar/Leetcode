class Solution:
    def robotWithString(self, s: str) -> str:

        char_freq=Counter(s)
        t_stack=[]
        paper=[]

        for ch in s:
           
            t_stack.append(ch)

            if char_freq[ch]==1:
                del char_freq[ch]
            else:
                char_freq[ch]-=1
            
            while t_stack and char_freq and t_stack[-1]<=min(char_freq):
                paper.append(t_stack.pop())


        while t_stack:
            paper.append(t_stack.pop())
        
        return ''.join(paper)

                





                
