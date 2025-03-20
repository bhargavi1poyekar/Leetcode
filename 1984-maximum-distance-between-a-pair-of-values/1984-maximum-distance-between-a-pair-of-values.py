class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        def binary_search(target, left):
            right = len(nums2)-1

            while left <= right:
                mid = (left + right)//2
                if nums2[mid] < target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return left-1
        
        max_distance = 0
        for i in range(len(nums1)):
            j = binary_search(nums1[i], i)
            # print(j)
            max_distance = max(max_distance, j-i)
        
        return max_distance

        

