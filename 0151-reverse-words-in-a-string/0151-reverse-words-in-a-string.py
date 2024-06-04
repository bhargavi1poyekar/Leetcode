class Solution:
    def reverseWords(self, s: str) -> str:
        flag=0
        str2=[]
        s=s.strip()
        length=len(s)
        for i in range(length):
            if s[i] == ' ' and (i!=0 and i!=length-1):
                flag=1
            elif s[i]!=' ' and flag==1:
                str2.append(' ')
                str2.append(s[i])
                flag=0
            elif s[i]!=' ' and flag==0:
                str2.append(s[i])
        
        
        str2=''.join(str2)
        str2=str2.split(' ')
        
        return ' '.join(str2[::-1])    
