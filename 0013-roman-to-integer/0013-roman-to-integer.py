class Solution:
    def romanToInt(self, s: str) -> int:
        rti={'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000}

        answer=0
        for i in range(len(s)-1):
            if rti[s[i]]<rti[s[i+1]]:
                answer-=rti[s[i]]
            else:
                answer+=rti[s[i]]
        
        return answer+rti[s[-1]]






