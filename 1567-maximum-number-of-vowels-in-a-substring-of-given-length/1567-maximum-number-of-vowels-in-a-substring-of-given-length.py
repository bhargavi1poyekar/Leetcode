class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels={'a':1,'e':1,'i':1,'o':1,'u':1}
        
        count_vow=0
        for i in range(k):
            if s[i] in vowels:
                count_vow+=1
        
        max_count=count_vow
        for i in range(k,len(s)):
            if s[i] in vowels:
                count_vow+=1
            if s[i-k] in vowels:
                count_vow-=1
            max_count=max(max_count,count_vow)

        return max_count

