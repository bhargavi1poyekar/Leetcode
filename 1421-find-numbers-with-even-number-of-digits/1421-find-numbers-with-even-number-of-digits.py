class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def count_digit(num):
            count=0
            while(num):
                num=num//10
                count+=1
            
            return count
        
        even_count=0

        for num in nums:
            if count_digit(num)%2==0:
                even_count+=1
        
        return even_count