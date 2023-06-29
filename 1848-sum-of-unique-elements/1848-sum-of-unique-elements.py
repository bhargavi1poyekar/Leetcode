class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:

        unique=collections.Counter(nums)
        
        sum=0
        for i in unique:
            if unique[i]==1:
                sum+=i
        return sum