class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count=collections.Counter(nums)
        max_freq=max(nums_count.values())

        buckets=[[] for i in range(max_freq)]

        for i in nums_count:
            buckets[nums_count[i]-1].append(i)

        ans=[]
        for i in range(len(buckets)-1,-1,-1):
            if k==0:
                break
            for num in buckets[i]:
                ans.append(num)
                k-=1

        return(ans)