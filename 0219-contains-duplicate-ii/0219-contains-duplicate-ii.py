class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hash_idx=Counter()

        for i in range(len(nums)):
            if nums[i] in hash_idx:
                if abs(i-hash_idx[nums[i]])<=k:
                    return True
                    
            hash_idx[nums[i]]=i
        
        return False