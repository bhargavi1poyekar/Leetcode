class Solution:
    def compress(self, chars: List[str]) -> int:
        n=len(chars)

        if n==1:
            return 1
        
        ptr1=0
        ptr2=1
        index=0
        count=1
        while(ptr2<n):
            if chars[ptr1]!=chars[ptr2]:
                chars[index]=chars[ptr1]
                index+=1
                if count>1 and count<10:
                    chars[index]=str(count)
                    index+=1
                elif count>=10:
                    chars[index:index+len(str(count))]=str(count)
                    index+=len(str(count))
                count=0
                ptr1=ptr2
            count+=1
            ptr2+=1
        
        chars[index]=chars[ptr1]
        index+=1
        if count>1 and count<10:
            chars[index]=str(count)
            index+=1
        elif count>=10:
            
            chars[index:index+len(str(count))]=str(count)
            index+=len(str(count))
        
        
        return index