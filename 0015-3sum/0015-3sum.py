class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []

        def two_sum(arr, target):
            start = 0
            end = len(arr) - 1
            triplets = []

            while start < end:
                if arr[start] + arr[end] == target:
                    triplets.append([arr[start], arr[end], -target])
                    start += 1
                    end -= 1

                    while arr[start] == arr[start - 1] and start < end:
                        start += 1  

                elif arr[start] + arr[end] > target:
                    end -= 1
                else:
                    start += 1
            
            return triplets

        
        for i in range(len(nums)-1):
            if nums[i] > 0:
                break
            elif i != 0 and nums[i] != nums[i-1]:
                ans.extend(two_sum(nums[i+1:], -nums[i]))
            elif i==0:
                ans.extend(two_sum(nums[i+1:], -nums[i]))
        
        return ans

       