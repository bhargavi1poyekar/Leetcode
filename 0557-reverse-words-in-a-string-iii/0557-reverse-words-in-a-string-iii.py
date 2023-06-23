class Solution:
    def reverseWords(self, s: str) -> str:

        s_list=s.split(' ')

        for words in range(len(s_list)):
            s_list[words]=s_list[words][::-1]
        
        return ' '.join(s_list)