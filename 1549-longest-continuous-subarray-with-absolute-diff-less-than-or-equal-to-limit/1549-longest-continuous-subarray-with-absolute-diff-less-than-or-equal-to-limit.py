class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ascend=deque()
        descend=deque()

        left=ans=0

        for right in range(len(nums)):

            while ascend and ascend[-1]>nums[right]:
                ascend.pop()
            while descend and descend[-1]<nums[right]:
                descend.pop()

            ascend.append(nums[right]) 
            descend.append(nums[right])

            if descend[0]-ascend[0]>limit:
                if descend[0]==nums[left]:
                    descend.popleft()
                elif ascend[0]==nums[left]:
                    ascend.popleft()

                left+=1

            ans=max(ans,right-left+1) 
        
        return ans