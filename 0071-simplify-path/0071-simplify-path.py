class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        Understand:

        Given -> abs path -> begins with slash. 
        Transform abs path to simplified canonical path. 

        single period -> curr directory. 

        double period -> previos dir

        multiple slash -> single slash

        anything that doesn't match -> are dir/ file names. 

        path must start with slash, and dir separated by slash. 

        Match: Stack -> to go back to prev directory. 

        Plan:

        Since all dir/file are separated by '/' -> split string on '/'. 

        Now if the char -> is . or empty -> it means we shouldn't do anything. Because it means current directory. 

        if .. -> then go to previous directory -> pop from stack. 

        else -> anything -> then we just add to stack -> as it is valid directory name
        '''

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
        
        '''
        Time Complexity: O(N)
        Space COmplexity: O(N)
        '''


