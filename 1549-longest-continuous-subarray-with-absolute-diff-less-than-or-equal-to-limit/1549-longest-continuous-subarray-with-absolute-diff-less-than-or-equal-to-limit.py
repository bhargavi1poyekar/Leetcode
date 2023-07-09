class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        min_q=deque()
        max_q=deque()
        left=0
        max_length=0

        for right in range(len(nums)):

            while min_q and min_q[-1]>nums[right]:
                min_q.pop()
            min_q.append(nums[right])

            while max_q and max_q[-1]<nums[right]:
                max_q.pop()
            max_q.append(nums[right])

            while max_q and min_q and max_q[0]-min_q[0]>limit:
                if min_q[0]==nums[left]:
                    min_q.popleft()
                
                if max_q[0]==nums[left]:
                    max_q.popleft()
                left+=1
            
            max_length=max(max_length,right-left+1)
        
        return max_length

