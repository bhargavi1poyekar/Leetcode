class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(left,right,target):
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1

            return -1

        n=len(nums)
        left,right=0,n-1

        while left<=right:
            mid=(left+right)//2
            if nums[mid]>nums[-1]:
                left=mid+1
            else:
                right=mid-1
        
        pivot=left

        left_half=binary_search(0,pivot-1,target)
        if left_half!=-1:
            return left_half
        
        return binary_search(pivot,n-1,target)


        
