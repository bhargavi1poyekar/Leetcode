class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        # s_list=list(s)
        # n=len(s)
        # left=0
        # right=n-1

        # while(left<=right):
            
        #     if not s_list[left].isalpha():
        #         left+=1
            
        #     if not s_list[right].isalpha():
        #         right-=1
            
        #     elif s_list[left].isalpha() and s_list[right].isalpha():
        #         s_list[left],s_list[right]=s_list[right],s_list[left]
        #         left+=1
        #         right-=1 

           

        
        # return ''.join(s_list)
            
        
        letters=[char for char in s if char.isalpha()]

        res=[]

        for char in s:
            if char.isalpha():
                res.append(letters.pop())
            else:
                res.append(char)
        
        return ''.join(res)