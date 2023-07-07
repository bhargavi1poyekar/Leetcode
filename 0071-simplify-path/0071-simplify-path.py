class Solution:
    def simplifyPath(self, path: str) -> str:

        stack_path=[]

        for direc in path.split('/'):
            # print(direc)

            if direc=='..':
                if stack_path:
                    stack_path.pop()
            
            elif direc=='.' or direc=='':
                continue
            
            else:
                stack_path.append(direc)
            

        return '/' + '/'.join(stack_path)
