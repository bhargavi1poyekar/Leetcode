class Solution:
    def largestPalindromic(self, num: str) -> str:
        num_count=Counter(num)
        start=''
        middle=''

        for i in range(9,0,-1):
            if num_count[str(i)]>=2:
                start+=(str(i)*(num_count[str(i)]//2))
        
        if start and num_count['0']>=2:
            start+=('0'*(num_count['0']//2))
        
        for i in range(9,-1,-1):
            if num_count[str(i)]%2==1:
                middle=str(i)
                break
        
        if not start and not middle:
            middle='0'
        
        return start+middle+start[::-1]