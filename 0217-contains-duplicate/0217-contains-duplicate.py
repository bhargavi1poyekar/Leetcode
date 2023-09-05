class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hash=Counter(nums)

        for i in hash:
            if hash[i]>=2:
                return True
        
        return False