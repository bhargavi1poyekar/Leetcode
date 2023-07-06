class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:

        queue=deque()

        count=len(nums)-k

        for num in nums:
            # print(queue)
            while(queue and queue[-1]>num and count):
                queue.pop()
                count-=1
            
            queue.append(num)
        
        return(list(queue)[:k])
