class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        def getMedian(max_heap,min_heap,win_size):
            if win_size%2==1:
                return -max_heap[0]
            else:
                return (-max_heap[0]+min_heap[0])/2
        
        median_answer=[]
        remove_count=Counter()
        min_heap=[]
        max_heap=[]

        for i in range(k):
            heapq.heappush(max_heap,-nums[i])

        for i in range(k//2):
            heapq.heappush(min_heap,-heapq.heappop(max_heap))
        
        median_answer.append(getMedian(max_heap,min_heap,k))

        for i in range(k,len(nums)):
            outgoing=nums[i-k]
            incoming=nums[i]

            balance=-1 if outgoing<=-max_heap[0] else 1
            remove_count[outgoing]+=1

            if incoming <=-max_heap[0]:
                heapq.heappush(max_heap,-incoming)
                balance+=1
            else:
                heapq.heappush(min_heap,incoming)
                balance-=1
            
            if balance<0:
                heapq.heappush(max_heap,-heapq.heappop(min_heap))
            elif balance>0:
                heapq.heappush(min_heap,-heapq.heappop(max_heap))
            
            while max_heap and remove_count[-max_heap[0]]>0:
                remove_count[-max_heap[0]]-=1
                heapq.heappop(max_heap)
            
            while min_heap and remove_count[min_heap[0]]>0:
                remove_count[min_heap[0]]-=1
                heapq.heappop(min_heap)
            
            median_answer.append(getMedian(max_heap,min_heap,k))

        
        return median_answer



        

