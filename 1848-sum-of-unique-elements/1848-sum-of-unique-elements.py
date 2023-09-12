class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:

        count=Counter(nums)
        sum=0
        for item in count:
            if count[item]==1:
                sum+=item
        return sum
        