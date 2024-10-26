class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def two_sum(arr, target):
            left = 0
            right = len(arr) - 1
            triplets = []
            while left < right:
                if arr[left] + arr[right] == target:
                    triplets.append([arr[left], arr[right], -target])
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left-1]:
                        left += 1
                
                elif arr[left] + arr[right] > target:
                    right -= 1
                else:
                    left += 1
            
            return triplets
        
        nums.sort()
        results = []

        for i in range(len(nums)-1):
            if nums[i] > 0:
                continue
            elif i != 0 and nums[i-1] != nums[i]:
                results.extend(two_sum(nums[i+1:], -nums[i]))
            elif i == 0:
                results.extend(two_sum(nums[i+1:], -nums[i]))
        
        return results



            



                    

    
        



        