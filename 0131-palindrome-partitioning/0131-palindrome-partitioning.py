class Solution:
    def partition(self, s: str) -> List[List[str]]:

        ans=[]

        def is_palindrome(string,start,end):

            while start<end:
                if string[start]!=string[end]:
                    return False
                start+=1
                end-=1
            return True
        
        def backtrack(start,curr):
            if start>=len(s):
                ans.append(list(curr))
                return 

            for i in range(start, len(s)):
                if is_palindrome(s,start,i):
                    curr.append(s[start:i+1])
                    backtrack(i+1,curr)
                    curr.pop()
        
        backtrack(0,[])
        return ans