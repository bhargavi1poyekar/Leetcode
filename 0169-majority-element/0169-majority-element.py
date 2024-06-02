class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hash_count = {}
        majority_count = len(nums)//2 
        
        for num in nums:
            if num in hash_count:
                hash_count[num] += 1
            else:
                hash_count[num] = 1

        for num in hash_count:
            if hash_count[num] > majority_count:
                return num


        