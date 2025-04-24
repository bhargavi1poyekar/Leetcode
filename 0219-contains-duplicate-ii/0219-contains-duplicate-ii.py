class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ''' 
        Understand: Given an int arr nums and k. 
        return True if two indices i, j have same val and abs(i - j) <= k

        Match: Hash dict -> keep track of elements encountered. 

        Plan:

        While traversing the arra -> we check if element is already seen, if yes, then we check the abs condition is true or not. if not, then we replace the index of the element in dict with curr elements index -> because the abs diff should be <= k, so anyway, if we are going to find, next j, then i should be the max(i, j)
        '''

        hash_seen = {}

        for j, num in enumerate(nums):
            if num in hash_seen:
                i = hash_seen[num]
                if abs(i-j) <= k:
                    return True
                else:
                    hash_seen[num] = j
            else:
                hash_seen[num] = j
        
        return False

        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''

