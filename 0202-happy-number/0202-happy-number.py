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