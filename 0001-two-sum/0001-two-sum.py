
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}

        for i, num in enumerate(nums):
            if num in pair:
                return [i, pair[num]]
            pair[target-num] = i
        
        
