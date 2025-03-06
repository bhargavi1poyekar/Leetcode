class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        index_map = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in index_map:
                return [i, index_map[diff]]
            else:
                index_map[nums[i]] = i
        
         