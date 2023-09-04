class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        def twoSum(nums,target):
            
            # print("hello")
            left=0
            right=len(nums)-1
            
            while left<right:
                if nums[left]+nums[right]==target:
                    ans.append([nums[left],nums[right],-target])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                elif nums[left]+nums[right]<target:
                    left+=1
                else:
                    right-=1
            
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            if nums[i]>0:
                print("hello")
                break
            elif i!=0 and nums[i]!=nums[i-1]:
                twoSum(nums[i+1:],-nums[i])
            elif i==0:
                twoSum(nums[i+1:],-nums[i])
        
        return ans


