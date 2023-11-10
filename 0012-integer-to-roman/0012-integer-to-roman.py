class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        romanint=  {1:'I',
                     4:'IV',
                     5:'V',
                     9:'IX',
                     10:'X',
                     40:'XL',
                     50:'L',
                     90:'XC',
                     100:'C',
                     400:'CD',
                     500:'D',
                     900:'CM',
                     1000:'M'}
        
        rom=[]
        numerals=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        rem=num
        i=0
        while i<len(numerals):
            print(i)
            if rem==0:
                break
            if rem>=numerals[i]:
                rom.append(romanint.get(numerals[i]))
                rem=rem-numerals[i]
                i=i-1
            i=i+1        
                
        
        return(''.join(rom))
                    
    