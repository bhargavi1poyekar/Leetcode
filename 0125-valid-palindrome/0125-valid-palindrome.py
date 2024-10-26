class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_lower = s.lower()
        s_filter = ''
        for i in s_lower:
            if i.isalnum():
                s_filter += i
            
        left = 0
        right = len(s_filter) - 1

        while left < right:
            if s_filter[left] != s_filter[right]:
                return False
            left += 1
            right -= 1
        
        return True
