class Solution:
    def isHappy(self, n: int) -> bool:

        num=n
        numsum=set()
        
        while(num!=1 and num not in numsum):
            numsum.add(num)
            digi_sq_sum=0
            while(num!=0):
                rem=num%10
                digi_sq_sum+=rem*rem
                num=num//10
            # print(digi_sq_sum)
            
            num=digi_sq_sum
        
        if num==1:
            return True
        return False
        

            