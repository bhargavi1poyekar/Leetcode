class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def check(divisor):
            div_sum=0
            for num in nums:
                div_sum+=ceil(num/divisor)
            
            return div_sum<=threshold

        left=1
        right=max(nums)

        while left<=right:
            mid=(left+right)//2

            if check(mid):
                right=mid-1
                
            else:
                left=mid+1
        
        return right+1



        