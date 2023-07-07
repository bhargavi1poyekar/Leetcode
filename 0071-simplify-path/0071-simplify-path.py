class Solution:
    def simplifyPath(self, path: str) -> str:

        stack_path=[] # stack to store directories

        for direc in path.split('/'): # split the path on /

            # go to parent directory 
            if direc=='..':
                if stack_path:
                    stack_path.pop()
            
            # stay in curr directory 
            elif direc=='.' or direc=='':
                continue
            
            # else add the directory name in stack
            else:
                stack_path.append(direc)
        
        # starts with /
        return '/' + '/'.join(stack_path)
