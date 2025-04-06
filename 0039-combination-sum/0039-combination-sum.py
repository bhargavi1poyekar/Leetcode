class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        Understanding:

        arr -> distinct integers and target
        return : list of all unique combinations of candidates where they sum to target. 

        return in any order. 
        same number -> unlimited number of times but combination should be unique. 

        test cases -> less than 150 combinations. 

        Match: Can use Backtracking -> input is small. 
        unique combinations. but same number multiple times. 

        Plan:

        function -> index (curr index position), curr combination

        first base case -> curr sum > target
        curr combination sum == target
        curr sum > target -> return 
        if curr combination sum == target: 
            add it to all combinations and then return. 

        index wont be out of boundary -> because we are sending curr i -> which is always inside boundary.  (i, len(candidates))

        Then again loop over index till end of candidates. 
        add curr num to combination, and call recursive function. 

        backtrack by removing the current num from the combination. 
        '''

        # Implement

        def backtrack(curr_i, curr):
            if sum(curr) == target:
                combinations.append(curr[:])
                return

            if sum(curr) > target:
                return

            for i in range(curr_i, len(candidates)):
                curr.append(candidates[i])
                backtrack(i, curr)
                curr.pop()
        
        combinations = []
        backtrack(0, [])
        return combinations

        '''
        Evaluation:
        Time Complexity: O (N^(T/M + 1)) -> T (target val), M (min val among candidate)
        Space Complexity: O(T/M) -> Num of recursive calls -> stack overhead 
        and O(T/M) -> combination of numbers. 
        '''