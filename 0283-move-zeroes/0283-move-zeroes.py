class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr1=0
        n=len(nums)
        
        for ptr2 in range(n):
            if nums[ptr2]!=0:
                temp=nums[ptr2]
                nums[ptr2]=nums[ptr1]
                nums[ptr1]=temp
                ptr1+=1

        return nums