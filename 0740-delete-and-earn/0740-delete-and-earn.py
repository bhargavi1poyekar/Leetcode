class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        points = Counter()
        max_num = 0

        for num in nums:
            points[num] += num
            max_num = max(max_num, num)
        
        dp = [0] * (max_num + 1)

        dp[0] = 0
        dp[1] = points[1]

        for num in range(2, max_num + 1):
            dp[num] = max(dp[num-1], dp[num-2] + points[num])

        return dp[max_num] 


