class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        '''
        Understand: sorted number in ascending order. 

        find 2 nums -> add up to target. 

        return indices -> added by 1 -> since 1-indexed array. 

        only 1 solution. cannot use same element twice. 

        QUest:

        number with no solution ?  -> no there will be a solution. 
        can there be duplicate numbers -> no
        can there be negative integers -> yes

        what if there is exact 1 number == target? no. 

        Match:

        Since numbers are sorted. and we need the sum to be target. 
        We can use 2 pointers -> one at the start, other at the end. 

        Plan:

        left = begin
        right = end

        till they are equal/overlap:
            we check their sum -> == target -> return indices. 
            if not , is sum> target -> dec right pointer. 
            if sum < target -> inc left pointer. 
        
        if no solution, just return [-1, -1]
        '''

        # Implementation:

        left = 0
        right = len(numbers) - 1

        while left <= right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum > target:
                right -= 1
            else:
                left += 1
        
        return [-1, -1]

        '''
        Review:
        [2, 7, 11, 15]  -> target = 9
        left = 0
        right = 1
        sum == 2 + 15 = 17 > target
         
        sum = 2 + 11 = 13 > target

        sum == 2 + 7 = 9 == target return [1,2]

        Evaluation:
        Time Complexity -> O(n)
        Space Complexity -> O(1)
        '''
