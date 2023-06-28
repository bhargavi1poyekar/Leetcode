class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        balloon='balloon'
        text_count=collections.Counter()
        for i in text:
            if i in balloon:
                text_count[i]+=1
        
        for i in balloon:
            if i not in text_count:
                text_count[i]=0
                
        text_count['l']//=2
        text_count['o']//=2

        return min(text_count.values())