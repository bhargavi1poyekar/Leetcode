class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        
        left=0
        right=len(letters)-1
        while(left<=right):
            mid=(right-left//2)
            if ord(letters[mid])>ord(target):
                right=mid-1
            else:
                left=mid+1
        
        if left==len(letters):
            return letters[0]
        return letters[left]


        