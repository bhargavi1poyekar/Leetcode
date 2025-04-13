class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        '''
        Understand:

        Given a arr. 

        if number of occurences of each value is unique. -> return True
        that means -> if there are 3 vals -> which can have duplicates in the list. 
        and their occurences are 2, 3, 2 -> then false -> as 2 is not unique. 
        if it is 2, 3, 1 -> then return True. 

        Match: -> hash for count. and then hash the values again. 

        Plan:
        Keep count of each val in hash. 
        Now take set of the values. Count of this set should match the count of unique values in original hash. Then the occurences are unique.  
        '''

        # Implementation

        arr_count = Counter(arr)
        count_set = set(arr_count.values())
        return len(count_set) == len(arr_count)

        '''
        Time Complexity: O(n)
        Space: O(N)
        '''

