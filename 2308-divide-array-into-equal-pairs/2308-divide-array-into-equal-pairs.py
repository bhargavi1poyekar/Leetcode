class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        num_count = Counter(nums)

        for num in num_count:
            # print(num_count[num])
            if num_count[num] % 2 == 1:
                return False
        
        return True