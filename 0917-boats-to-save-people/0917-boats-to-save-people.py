class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        ptr1=0
        ptr2=len(people)-1

        ans=0

        while ptr1<=ptr2:
            if people[ptr1]+people[ptr2]<=limit:
                ptr1+=1
            ptr2-=1
            ans+=1
        
        return ans