class Solution:
    def robotWithString(self, s: str) -> str:
        
        s_dict = Counter(s)
        t_stack = []
        paper = []

        for ch in s:
            s_dict[ch] -= 1
            if s_dict[ch] == 0:
                del s_dict[ch]
            
            t_stack.append(ch)
            
            while t_stack and s_dict and t_stack[-1] <= min(s_dict):
                paper.append(t_stack.pop())
        
        while t_stack:
            paper.append(t_stack.pop())

        return ''.join(paper)