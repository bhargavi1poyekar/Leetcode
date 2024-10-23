class Solution:
    def reverseWords(self, s: str) -> str:

        def reverse(word):
            left=0
            right=len(word)-1
            while(left<right):
                word[left], word[right] = word[right], word[left]
                left+=1
                right-=1

            return word
            
        s_list=s.split(' ')

        for i in range(len(s_list)):
            word=list(s_list[i])
            rev_word = reverse(word)
            s_list[i]=''.join(word)
           
        return ' '.join(s_list)