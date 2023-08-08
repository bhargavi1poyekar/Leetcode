class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def valid(subs):
            if len(subs)>3 or len(subs)==0:
                return False
            if len(subs)>1 and subs[0]=='0':
                return False
            if len(subs) and int(subs)>255:
                return False
            return True
    
        def backtrack(curr,index,dot_count):
            if dot_count==3:
                if valid(s[index:]):
                    ans.append(curr+s[index:])
                return
            
            for i in range(index, min(index+3, len(s))):
                if valid(s[index:i+1]):
                    backtrack(curr+s[index:i+1]+'.',i+1,dot_count+1)

        ans=[]
        backtrack('',0,0)
        return ans
