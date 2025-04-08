class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return -1

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1 
            else:
                right = mid - 1
        
        pivot = left
        # print(pivot)

        left_search = binary_search(0, pivot - 1)
        if left_search != -1:
            return left_search
        return binary_search(pivot, len(nums)-1)
        


