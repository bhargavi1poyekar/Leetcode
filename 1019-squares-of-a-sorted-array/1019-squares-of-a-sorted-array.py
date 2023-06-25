class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n=len(nums) 
        left=0
        right=n-1
        
        squared=[0 for i in range(n)]
        for i in range(n-1,-1,-1):
            if abs(nums[left])>abs(nums[right]):
                squared[i]=nums[left]*nums[left]
                left+=1
            else:
                squared[i]=nums[right]*nums[right]
                right-=1
        return squared