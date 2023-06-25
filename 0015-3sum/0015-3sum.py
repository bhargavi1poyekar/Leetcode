class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans=[] # Final Answer

        nums=sorted(nums) # Sort for two sum
 
        for i in range(len(nums)):
            if nums[i]>0: 
                # No later numbers will give negative sum to become 0
                break
            elif i!=0 and nums[i]!=nums[i-1]:
                ans.extend(self.twoSum(nums[i+1:],-nums[i]))
                # if i not repeated, send for two sum, with remaining nums and target as negative of current num
            elif i==0:
                ans.extend(self.twoSum(nums[i+1:],-nums[i]))
        
        return ans


    
    def twoSum(self, nums,target):

        left=0
        right=len(nums)-1

        ans=[]
        while(left<right): # Till left and right overlap

            if nums[left]+nums[right]==target: # If correct triplet,
                ans.append([-target,nums[left],nums[right]]) 
                # Append to the triplets
                left+=1 
                right-=1

                while(left<right and nums[left]==nums[left-1]): 
                    # to avoid repeatation
                    left+=1

            elif nums[left]+nums[right]>target: 
                # If total greater than target
                right-=1

            else:
                left+=1

        return ans 