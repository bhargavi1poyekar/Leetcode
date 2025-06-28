class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def first_position(left, right):
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            
            return left
        
        def last_position(left, right):
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            
            return left - 1
        
        ans = []
        first_index = first_position(0, len(nums))
        if not 0 <= first_index < len(nums):
            return [-1, -1]
        elif nums[first_index] != target:
            return [-1, -1]
        else:
            ans.append(first_index)
        
        ans.append(last_position(0, len(nums)))
        return ans
        