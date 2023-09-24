class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        

        word_0=strs[0]

        for i in range(len(word_0)):
            for word in strs[1:]:
                if i==len(word) or word[i]!=word_0[i]:
                    return word_0[0:i]

        return word_0