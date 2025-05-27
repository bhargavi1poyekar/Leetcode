class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        def twoSum(nums, target):

            start = 0
            end = len(nums) - 1

            triplets = []

            while start < end:
                sum = nums[start] + nums[end]
                if sum == target:
                    triplets.append([nums[start], nums[end], -target])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                
                elif sum > target:
                    end -= 1
                else:
                    start += 1
            
            return triplets


        nums.sort()
        ans = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i != 0 and nums[i] != nums[i-1]:
                ans.extend(twoSum(nums[i+1:], -nums[i]))
            elif i == 0:
                ans.extend(twoSum(nums[i+1:], -nums[i]))
        
        return ans

