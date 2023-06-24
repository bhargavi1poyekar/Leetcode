class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        # prefix_sum=[nums[0]]

        # n=len(nums)
        # for i in range(1,n):
        #     prefix_sum.append(nums[i]+prefix_sum[i-1])

        # count=0
        # for i in range(n-1):
        #     if prefix_sum[i]>=prefix_sum[n-1]-prefix_sum[i]:
        #         count+=1
        
        # return count

        left=right=count=0

        n=len(nums)
        total=sum(nums)

        for i in range(len(nums)-1):
            left+=nums[i]
            right=total-left

            if left>=right:
                count+=1
        
        return count

