class Solution:
    def minOperations(self, nums: List[int]) -> int:
        queue = deque()
        count = 0

        for i in range(len(nums)):
            while queue and i > queue[0] + 2:
                queue.popleft()
            
            if (nums[i] + len(queue)) % 2 == 0:
                if i + 2 >= len(nums):
                    return -1
                
                count += 1
                queue.append(i)
        
        return count