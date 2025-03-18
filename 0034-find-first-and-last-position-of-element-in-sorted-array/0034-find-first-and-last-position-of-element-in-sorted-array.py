class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [-1, -1]

        def first_binary_search(target):
            left = 0
            right = len(nums)

            while left < right:
                mid = (left + right ) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            
            return left

        def last_binary_search(target):
            left = 0
            right = len(nums)

            while left < right:
                mid = (left + right ) // 2
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            
            return left

        first = first_binary_search(target)
        last = last_binary_search(target)

        if first < len(nums) and nums[first] == target:
            return [first, last-1]
        return [-1, -1]