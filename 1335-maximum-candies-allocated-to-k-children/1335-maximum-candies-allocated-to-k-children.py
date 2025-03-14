class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def distribute(max_candy):
            # print(f'max_candy:{max_candy}')
            count_children=0
            for candy in candies:
                count_children+=candy//max_candy
            return count_children>=k
        

        left=1
        # right=max(candies)
        right=sum(candies)//k

        while left<=right:
            # print(left,right)
            mid=(left+right)//2

            if distribute(mid):
                left=mid+1
            else:
                right=mid-1
        
        return right