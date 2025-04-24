class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Understand:

        Given -> unsorted array of int -> nums. 
        return length of longest consecutive elements seq. 

        Solution should -> O(N)
        Match : convert list to sets -> to check existence of element in O(1) complexity. 

        Plan:

        while we traverse nums:
            we check if nums-1 also in set -> if yes, then we might have already onsidered nums in that sequence. 

            if nums-1 not in set, then seq starts from nums, 
            then while num + 1 in set, we keep on increasing the length of sequence. 

            and once the sequence end, we update max seq length. 
        '''

        num_set = set(nums)
        max_length = 0

        for num in num_set:
            if num - 1 not in num_set:
                seq = 1 
                while num + 1 in num_set:
                    seq += 1
                    num += 1
                max_length = max(max_length, seq)
        
        return max_length

        '''
        Time Complexity: O(N)
        Space COmplexity: O(N)
        '''