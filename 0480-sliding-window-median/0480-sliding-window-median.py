class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        def getMedian(max_heap,min_heap,win_size):
            # If odd numbers return maxheap top
            if win_size%2==1:
                return -max_heap[0]
            # If even return avg of max and min
            else: 
                return (-max_heap[0]+min_heap[0])/2
        
        median_answer=[] # Final answer of medians
        remove_count=Counter() # to keep count of outgoing elements, when they are at top, remove them.
        # also called lazy removing.
        
        min_heap=[]
        max_heap=[]
        
        # Put first window elements in heap 
        for i in range(k):
            heapq.heappush(max_heap,-nums[i])

        # Remove half elements from max and put in min
        for i in range(k//2):
            heapq.heappush(min_heap,-heapq.heappop(max_heap))
        
        # Get first median
        median_answer.append(getMedian(max_heap,min_heap,k))

        # Now window starts sliding
        for i in range(k,len(nums)):
            outgoing=nums[i-k] # Element to be removed
            incoming=nums[i] # Element added

            # If element from max_heap, balance becomes -1 else if from min, balance is 1 
            balance=-1 if outgoing<=-max_heap[0] else 1 
            remove_count[outgoing]+=1 # Add count for outgoing

            # If incoming from first half
            if incoming <=-max_heap[0]:
                heapq.heappush(max_heap,-incoming) # Put in max heap
                balance+=1 # Increase balance
            else: # If from second half
                heapq.heappush(min_heap,incoming) # Put in min_heap
                balance-=1 # Decrease balance
            
            # If balance less than 0, it means min has more elements than max
            if balance<0:
                heapq.heappush(max_heap,-heapq.heappop(min_heap))
            
            # If balance greater than 0, it means max has more elements than min
            elif balance>1:
                heapq.heappush(min_heap,-heapq.heappop(max_heap))
            
            # Now if the max and min tops are elements to be removed, remove them.
            while max_heap and remove_count[-max_heap[0]]>0:
                remove_count[-max_heap[0]]-=1
                heapq.heappop(max_heap)
            
            while min_heap and remove_count[min_heap[0]]>0:
                remove_count[min_heap[0]]-=1
                heapq.heappop(min_heap)
            
            # Get current window median.
            median_answer.append(getMedian(max_heap,min_heap,k))

        
        return median_answer



        

