class Solution:
    def intToRoman(self, num: int) -> str:
        roman_to_int={
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10:'X',
            40:'XL',
            50:"L",
            90:'XC',
            100:'C',
            400:'CD',
            500:'D',
            900:'CM',
            1000:'M',
        }

        int_num=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman=''
        i=0
        while i<len(int_num):
            # print(roman)
            if num==0:
                break
            elif num>=int_num[i]:
                roman+=roman_to_int[int_num[i]]
                num-=int_num[i]
                i-=1
            i+=1
        
        return(roman)




