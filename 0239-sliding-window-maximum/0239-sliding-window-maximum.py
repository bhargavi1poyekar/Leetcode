class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:   

        queue=deque()
        max_window=[]

        for curr in range(len(nums)):
            
            while(queue and nums[queue[-1]]<nums[curr]):
                queue.pop()

            queue.append(curr)

            if queue[0]+k==curr:
                queue.popleft()
            
            if curr>=k-1:
                max_window.append(nums[queue[0]])
            
            # print(curr, queue, max_window)
        
        return(max_window)





        

        