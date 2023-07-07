class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        inc_queue=deque()
        dec_queue=deque()
        left,max_length=0,0

        for right in range(len(nums)):
            while(inc_queue and inc_queue[-1]>nums[right]):
                inc_queue.pop()
            
            inc_queue.append(nums[right])
        
            while(dec_queue and dec_queue[-1]<nums[right]):
                dec_queue.pop()
            
            dec_queue.append(nums[right])

            while(dec_queue[0]-inc_queue[0]>limit):
                if inc_queue[0]==nums[left]:
                    inc_queue.popleft()
                
                if dec_queue[0]==nums[left]:
                    dec_queue.popleft()
                
                left+=1
            
            max_length=max(max_length,right-left+1)
        
        return max_length
                

                



            
        