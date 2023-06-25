class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans=[]

        nums=sorted(nums)

        for i in range(len(nums)):
            if nums[i]>0:
                break
            elif i!=0 and nums[i]!=nums[i-1]:
                ans.extend(self.twoSum(nums[i+1:],-nums[i]))
            elif i==0:
                ans.extend(self.twoSum(nums[i+1:],-nums[i]))
        
        return ans


    
    def twoSum(self, nums,target):

        left=0
        right=len(nums)-1

        ans=[]
        while(left<right):

            if nums[left]+nums[right]==target:
                ans.append([-target,nums[left],nums[right]])
                left+=1
                right-=1

                while(left<right and nums[left]==nums[left-1]):
                    left+=1

            elif nums[left]+nums[right]>target:
                right-=1

            else:
                left+=1

        return ans 