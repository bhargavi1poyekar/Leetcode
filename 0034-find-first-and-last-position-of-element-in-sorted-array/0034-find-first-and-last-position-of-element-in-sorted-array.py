class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left, right=0, len(nums)-1
        leftmost_index=-1
        
        while left<=right:
            
            mid=(left+right)//2
            if nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                leftmost_index=mid
                right=mid-1
        
        if leftmost_index==-1:
            return [-1,-1]
        
        # print(leftmost_index)
        
        
        # find left boundary
        left, right=0, len(nums)
        
        while left<right:
            mid=(left+right)//2
            if nums[mid]>target:
                right=mid
            else:
                left=mid+1
        
        return [leftmost_index,left-1]