class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        Modulo = (10 ** 9) + 7

        odd_prefix_count = 0
        even_prefix_count = 1

        odd_sum_subarray = 0

        prefix_sum = 0

        for i in range(len(arr)):
            prefix_sum += arr[i]

            if prefix_sum % 2 == 0:
                even_prefix_count += 1
                odd_sum_subarray += odd_prefix_count
            else:
                odd_prefix_count += 1
                odd_sum_subarray += even_prefix_count

        
        return odd_sum_subarray % Modulo
