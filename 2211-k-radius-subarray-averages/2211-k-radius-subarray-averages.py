class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        prefix_sum=[0]
        num_in_win=2*k+1
        # ans=[0 for i in range(len(nums))]
        ans=[]

        for i in range(len(nums)):
            prefix_sum.append(nums[i]+prefix_sum[i])
        
        for i in range(len(nums)):
            if i-k<0 or i+k>=len(nums):
                ans.append(-1)
            else:
                ans.append((prefix_sum[i+k+1]-prefix_sum[i-k])//num_in_win)
                
        
        return ans

