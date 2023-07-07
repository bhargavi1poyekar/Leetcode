class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:   

        queue=deque() # monotonically decreasing queue
        max_window=[] # list to store max of windows

        for curr in range(len(nums)):
            
            while(queue and nums[queue[-1]]<nums[curr]): # To maintain decreasing queue
                queue.pop()

            queue.append(curr)  

            # If window has reached its limits and max has expired, remove the front (max)
            if queue[0]+k==curr: 
                queue.popleft()
            
            # if window is created. (i.e. there are k elements in the window)
            if curr>=k-1:
                max_window.append(nums[queue[0]])
        
        return(max_window)





        

        