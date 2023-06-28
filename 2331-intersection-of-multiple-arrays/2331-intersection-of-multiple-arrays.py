class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:

        count=collections.Counter()
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                # print(nums[i][j])
                count[nums[i][j]]+=1
        
        ans=[]
        for i in count:
            if count[i]==len(nums):
                ans.append(i)
            
        return sorted(ans)

