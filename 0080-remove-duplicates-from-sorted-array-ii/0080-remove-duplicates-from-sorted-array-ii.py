class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        ptr1=0
        ptr2=1

        count=1

        while(ptr2<len(nums)):

            if nums[ptr1]==nums[ptr2] and count<2:
                ptr1+=1
                nums[ptr1]=nums[ptr2]
                count+=1
                
            elif nums[ptr1]!=nums[ptr2]:
                ptr1+=1
                nums[ptr1]=nums[ptr2]
                count=1
            
            ptr2+=1
        
        return ptr1+1
