class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        Modulo = (10 ** 9) + 7

        odd_prefix_count = 0
        even_prefix_count = 1 # Sum 0. 

        sub_odd_count = 0

        prefix_sum = 0

        for num in arr:
            prefix_sum += num

            if prefix_sum % 2 == 0:
                even_prefix_count += 1
                sub_odd_count += odd_prefix_count
            else:
                odd_prefix_count += 1
                sub_odd_count += even_prefix_count

        
        return sub_odd_count % Modulo
