class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(string, start, end):
            left = start
            right = end

            while left <= right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            
            return True
        
        partitions = []

        def backtrack(i, arr):
            if i == len(s):
                partitions.append(arr[:])
                return 
            
            for j in range(i, len(s)):
                if is_palindrome(s, i, j):
                    arr.append(s[i:j+1])
                    backtrack(j+1, arr)
                    arr.pop()
            
        backtrack(0, [])
        return partitions
            
