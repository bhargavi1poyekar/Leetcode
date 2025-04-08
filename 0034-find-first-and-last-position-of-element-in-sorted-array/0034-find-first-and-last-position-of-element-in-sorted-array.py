class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def first_position():
            left = 0
            right = len(nums)

            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            
            return left
        
        def last_position():
            left = 0
            right = len(nums)

            while left < right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            
            return left
        
        ans = []
        first_index = first_position()
        if not 0 <= first_index < len(nums):
            return [-1, -1] 
        elif nums[first_index] != target:
            return [-1, -1]
        else:
            ans.append(first_index)
        
        ans.append(last_position()-1)
        return ans


