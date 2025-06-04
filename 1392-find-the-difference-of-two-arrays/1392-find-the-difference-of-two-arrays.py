class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        distinct_nums1 = []
        distinct_nums2 = []

        for num in nums1_set:
            if num not in nums2_set:
                distinct_nums1.append(num)
        
        for num in nums2_set:
            if num not in nums1_set:
                distinct_nums2.append(num)
        
        return [distinct_nums1, distinct_nums2]
        