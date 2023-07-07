class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        inc_queue=deque() # increasing queue for min 
        dec_queue=deque() # decreasing queue for max
        left,max_length=0,0 

        for right in range(len(nums)):

            # Maintain montonically increasing
            while(inc_queue and inc_queue[-1]>nums[right]):
                inc_queue.pop()
            
            inc_queue.append(nums[right])
        
            # Maintain montonically DEcreasing
            while(dec_queue and dec_queue[-1]<nums[right]):
                dec_queue.pop()
            
            dec_queue.append(nums[right])

            # If window condition not satsifed, remove older element.
            while(dec_queue[0]-inc_queue[0]>limit):
                if inc_queue[0]==nums[left]: # while removing, check it is current min 
                    inc_queue.popleft()
                
                if dec_queue[0]==nums[left]: # while removing, check it is current max
                    dec_queue.popleft()
                 
                left+=1 # decrease window size 
            
            max_length=max(max_length,right-left+1)
        
        return max_length
                

                



            
        