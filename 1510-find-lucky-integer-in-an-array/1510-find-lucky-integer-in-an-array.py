class Solution:
    def findLucky(self, arr: List[int]) -> int:

        freq=Counter(arr)

        max_lucky=-1
        for val in freq:
            if freq[val]==val:
                max_lucky=max(max_lucky,val)
            
        return max_lucky



        