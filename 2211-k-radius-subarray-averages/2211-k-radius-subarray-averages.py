class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums)<2*k:
            return [-1]*len(nums)

        total_count = (2 * k) + 1
        avgs = [-1] * len(nums)

        prefix_arr = [0]
        for i in range(len(nums)):
            prefix_arr.append(nums[i] + prefix_arr[i])
        
        for i in range(k, len(nums) - k):
            rad_sum = prefix_arr[i + k + 1] - prefix_arr[i - k]
            avgs[i] = rad_sum // total_count

        return(avgs) 
            