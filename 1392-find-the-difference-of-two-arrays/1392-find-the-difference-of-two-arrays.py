class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        nums1_hash = Counter(nums1)
        nums2_hash = Counter(nums2)

        nums1_distinct = []
        nums2_distinct = []

        for num in nums1_hash:
            if num not in nums2:
                nums1_distinct.append(num)
        
        for num in nums2_hash:
            if num not in nums1:
                nums2_distinct.append(num)
        
        return [nums1_distinct, nums2_distinct]

                