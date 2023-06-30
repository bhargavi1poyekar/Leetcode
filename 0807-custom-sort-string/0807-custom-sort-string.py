class Solution:
    def customSortString(self, order: str, s: str) -> str:

        s_count=collections.Counter(s)

        ans=[]
        for char in order:
            ans.append(char*s_count[char])
            del s_count[char]
        
        for i in s_count:
            ans.append(i*s_count[i])

        return ''.join(ans)

