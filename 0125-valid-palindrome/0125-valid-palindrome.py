class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_list = []
        for i in range(len(s)):
            if s[i].isalnum():
                s_list.append(s[i])


        start = 0
        end = len(s_list) - 1

        while start <= end:
            if s_list[start] != s_list[end]:
                return False

            start += 1
            end -= 1
        
        return True


