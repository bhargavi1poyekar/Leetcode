class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []

        for ch in path.split('/'):
            if ch == '.' or ch == '':
                continue
            elif ch == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        
        return '/' + '/'.join(stack)
        