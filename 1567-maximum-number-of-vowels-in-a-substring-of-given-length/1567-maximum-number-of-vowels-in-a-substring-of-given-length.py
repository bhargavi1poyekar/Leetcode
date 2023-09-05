class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels=set(['a','e','i','o','u'])

        left=0
        
        vow_count=0
        for right in range(k):
            if s[right] in vowels:
                vow_count+=1
            
        max_vow=vow_count
        
        for right in range(k,len(s)):
            if s[right] in vowels:
                vow_count+=1
            
            if s[left] in vowels:
                vow_count-=1
            left+=1
            
            max_vow=max(max_vow,vow_count)
        
        return max_vow
        