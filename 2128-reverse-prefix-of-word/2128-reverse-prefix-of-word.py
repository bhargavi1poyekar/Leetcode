class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        word_l=list(word)
        start=0
        for i in range(len(word_l)):

            if word_l[i]==ch:
                print(word_l)
                end=i
                while(start<end):
                    temp=word_l[end]
                    word_l[end]=word_l[start]
                    word_l[start]=temp
                    start+=1
                    end-=1
                break
            
        return ''.join(word_l)
