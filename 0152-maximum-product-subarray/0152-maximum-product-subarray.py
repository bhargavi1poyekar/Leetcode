class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        ans=max(nums) # default max element
        min_prod,max_prod=1,1 
        
        for i in nums:
            if i==0: # if multiplied with 0, prod becomes 0, hence we dont want to include it.
                min_prod,max_prod=1,1
                continue
            tmp=max_prod*i # max_prod changes, and we have to use it in min_prod calculation
            max_prod=max(tmp,min_prod*i,i)
            min_prod=min(tmp,min_prod*i,i)
            ans=max(ans,max_prod) # Finally, we decide, whether to use this element in product
        return ans
