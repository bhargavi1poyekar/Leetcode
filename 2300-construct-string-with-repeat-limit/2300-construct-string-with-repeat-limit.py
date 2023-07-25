class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:

        char_count=Counter(s)
        max_heap=[]

        for char in char_count:
            max_heap.append((-ord(char),char_count[char]))
        
        heapq.heapify(max_heap)
        lex_largest=''

        while max_heap:
            ascii_val,count=heapq.heappop(max_heap)
            char=chr(-ascii_val)
            # print(char,count)
            if not lex_largest or lex_largest[-1]!=char:
                lex_largest+=min(count,repeatLimit)*char
                if count>repeatLimit:
                    heapq.heappush(max_heap,(-ord(char),count-repeatLimit))
            else:
                if max_heap:
                    ascii2,count2=heapq.heappop(max_heap)
                    char2=chr(-ascii2)
                    lex_largest+=char2
                    if count2>1:
                        heapq.heappush(max_heap,(-ord(char2),count2-1))
                    heapq.heappush(max_heap,(-ord(char),count))
                
         
            
        return lex_largest