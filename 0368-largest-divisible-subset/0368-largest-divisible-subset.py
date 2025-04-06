class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        subsets = {-1: set()}  # Initialize with a dummy key to handle the first number

        nums.sort()
        
        for num in nums:
            max_subset = set()
            
            for k in subsets:
                if num % k == 0:
                    if len(subsets[k]) > len(max_subset):
                        max_subset = subsets[k]
            
            subsets[num] = max_subset | {num}
        
        return list(max(subsets.values(), key=len))