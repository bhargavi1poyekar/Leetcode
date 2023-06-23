class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        
        left=0
        right=n-1
        
        while left<right:
           
            if nums[left]%2==1 and nums[right]%2==0:
                temp=nums[left]
                nums[left]=nums[right]
                nums[right]=temp
                
            if nums[right]%2==1:
                right-=1
            
            if nums[left]%2==0:
                left+=1
            
        return nums