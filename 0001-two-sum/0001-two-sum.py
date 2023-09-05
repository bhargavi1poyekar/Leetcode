class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash={}
        for i in range(len(nums)):
            if nums[i] in hash:
                return [hash[nums[i]],i]
            else:
                hash[target-nums[i]]=i

        # print(hash)
