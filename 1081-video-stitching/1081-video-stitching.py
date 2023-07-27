class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        
        curr_end,num=0,0
        clips.sort(reverse=True)
        
        while curr_end<time:
            heap=[]
            while clips and clips[-1][0]<=curr_end:
                heappush(heap,-clips.pop()[1])
            if not heap: return -1
            curr_end=-heap[0]
            num+=1
        
        return num