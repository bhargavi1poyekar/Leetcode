class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hash_index = defaultdict()

        for j in range(len(nums)):
            if nums[j] in hash_index:
                i = hash_index[nums[j]]
                if abs(i - j) <= k:
                    return True

            hash_index[nums[j]] = j

        return False