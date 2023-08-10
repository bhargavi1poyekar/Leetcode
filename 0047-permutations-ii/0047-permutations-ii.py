class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def backtrack(curr, counter):
            if len(curr) == len(nums):
                ans.append(list(curr))
                return
        
            for num in counter:
                if counter[num]>0:
                    curr.append(num)
                    counter[num]-=1
                    backtrack(curr,counter)
                    counter[num]+=1
                    curr.pop()
                   
            
        ans = []
        counter=Counter(nums)
        backtrack([],counter)
        return ans

        