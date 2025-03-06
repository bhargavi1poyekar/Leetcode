class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hash_index = {}

        for i in range(len(nums)):
            if nums[i] in hash_index:
                if abs(hash_index[nums[i]] - i) <= k:
                    return True
            hash_index[nums[i]] = i
        
        return False