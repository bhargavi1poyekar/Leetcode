class Solution:
    def robotWithString(self, s: str) -> str:

        count=Counter(s)
        t_stack,ans=[],[]

        for ch in s:
            t_stack.append(ch)

            if count[ch]==1:
                del count[ch]
            else:
                count[ch]-=1
            
            while count and t_stack and min(count)>=t_stack[-1]:
                ans.append(t_stack.pop())
        
        while(t_stack):
            ans.append(t_stack.pop())
        
        return ''.join(ans)

                
