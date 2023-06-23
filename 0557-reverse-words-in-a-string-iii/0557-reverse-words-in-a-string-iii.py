class Solution:
    def reverseWords(self, s: str) -> str:

        # s_list=s.split(' ')

        # for words in range(len(s_list)):
        #     s_list[words]=s_list[words][::-1]
        
        # return ' '.join(s_list)

        s_list=s.split(' ')

        for i in range(len(s_list)):
            left=0
            right=len(s_list[i])-1
            words=list(s_list[i])
            while(left<right):
                temp=words[right]
                words[right]=words[left]
                words[left]=temp
                left+=1
                right-=1
            s_list[i]=''.join(words)
            
        return ' '.join(s_list)

