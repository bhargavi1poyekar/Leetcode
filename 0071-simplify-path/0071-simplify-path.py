class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []

        for ch in path.split('/'):
            # print(ch)
            if ch == '.' or ch == '':
                continue
            elif ch == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        
        # print(stack)
        return '/' + '/'.join(stack)
