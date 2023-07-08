class Solution:
    def calculate(self, s: str) -> int:

        stack=[]
        res,val=0,0
        sign=1

        for ch in s:

            if ch.isdigit():
                val=val*10+int(ch)
            
            elif ch=='+':
                res+=val*sign
                sign=1
                val=0
            
            elif ch=='-':
                res+=val*sign
                sign=-1
                val=0
            
            elif ch=='(':
                stack.append(res)
                stack.append(sign)
                res=0
                sign=1
            
            elif ch==')':
                res+=val*sign
                res*=stack.pop()
                res+=stack.pop()
                val=0

        return res+(sign*val)
                
