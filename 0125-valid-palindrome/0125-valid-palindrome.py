class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_list = []

        for ch in s:
            if ch.isalnum():
                s_list.append(ch.lower())
        
        start = 0
        end = len(s_list) - 1

        while start <= end:
            if s_list[start] != s_list[end]:
                return False
            start += 1
            end -= 1
        
        return True