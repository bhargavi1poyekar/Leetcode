class Solution:
    def isHappy(self, n: int) -> bool:

        sum_hash=set()

        while n!=1 and n not in sum_hash:
            sum_hash.add(n)
            dig_sum=0

            while n!=0:
                rem=n%10
                dig_sum+=rem*rem
                n=n//10
            
            n=dig_sum
        
        if n==1:
            return True
        return False


    # num=n
    #     numsum=set()
        
    #     while(num!=1 and num not in numsum):
    #         numsum.add(num)
    #         digi_sq_sum=0
    #         while(num!=0):
    #             rem=num%10
    #             digi_sq_sum+=rem*rem
    #             num=num//10
    #         # print(digi_sq_sum)
            
    #         num=digi_sq_sum
        
    #     if num==1:
    #         return True
    #     return False


        