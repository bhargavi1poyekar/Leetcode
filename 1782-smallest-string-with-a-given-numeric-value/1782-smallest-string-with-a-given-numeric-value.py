class Solution:
    def getSmallestString(self, n: int, k: int) -> str:

        string=['a' for i in range(n)]
        k-=n
        ptr=n-1

        while k:
            k+=1
            if k/26>=1:
                string[ptr]='z'
                ptr-=1
                k-=26
            else:
                string[ptr]=chr(k+96)
                k-=k
        
        return ''.join(string)
        
