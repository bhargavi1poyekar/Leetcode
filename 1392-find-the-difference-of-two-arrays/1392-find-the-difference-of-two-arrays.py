class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        nums1_set = set(nums1)
        nums2_set = set(nums2)

        dist_nums1 = []
        dist_nums2 = []

        for num in nums1_set:
            if num not in nums2_set:
                dist_nums1.append(num)
        
        for num in nums2_set:
            if num not in nums1_set:
                dist_nums2.append(num)
        
        return [dist_nums1, dist_nums2]


        