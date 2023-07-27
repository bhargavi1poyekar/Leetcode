class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:

        if finalSum%2==1:
            return []

        curr_even=2
        split=[]
        while finalSum:
            if curr_even<=finalSum and (finalSum-curr_even)==0 or (finalSum-curr_even>curr_even):
                finalSum-=curr_even
                split.append(curr_even)
                curr_even+=2
            else:
                curr_even=finalSum
        return(split)
    