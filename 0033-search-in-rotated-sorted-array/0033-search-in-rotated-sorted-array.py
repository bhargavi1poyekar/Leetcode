class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(left, right):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid
        
        pivot = left

        first_index = binary_search(0, left-1)
        if first_index != -1:
            return first_index
        return binary_search(left, len(nums)-1)
