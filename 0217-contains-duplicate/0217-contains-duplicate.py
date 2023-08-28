class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hash={}

        for num in nums:
            if num in hash:
                return True
            else:
                hash[num]=1
        
        return False


        # nums=sorted(nums)

        # for i in range(1,len(nums)):
        #     if nums[i]==nums[i-1]:
        #         return True
        
        # return False