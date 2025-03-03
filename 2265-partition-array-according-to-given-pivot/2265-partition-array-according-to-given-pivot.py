class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        n = len(nums)
        less_ptr = 0
        great_ptr = n-1

        rearrange_arr = [0] * n
        start_index = 0 
        count_pivot = 0

        while less_ptr < n:
            if nums[less_ptr] < pivot:
                rearrange_arr[start_index] = nums[less_ptr]
                start_index += 1
            elif nums[less_ptr] == pivot:
                count_pivot += 1
            less_ptr += 1
        
        end_index = n-1
        while great_ptr > -1:
            if nums[great_ptr] > pivot:
                rearrange_arr[end_index] = nums[great_ptr]
                end_index -= 1
            great_ptr -= 1

        pivot_arr = [pivot]*(end_index + 1 - start_index)
        rearrange_arr[start_index:end_index+1] = [pivot]*(end_index + 1 - start_index)
        # print()
        # print(pivot_arr)
        return rearrange_arr
        


