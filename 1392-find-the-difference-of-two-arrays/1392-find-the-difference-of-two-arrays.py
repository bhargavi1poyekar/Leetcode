class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        '''
        Understand

        Given two -> 0-indexed arrays nums1 and nums2 -> 
        return list answer of size 2

        answer[0] = list of all distinct integers in nums1 not present in nums2
        answer[1] = list of all distinct integers in nums2 not present in nums1

        Match: Set to get distinct elements in nums 1 and 2, then traverse to check if a certain element present in both. 

        Plan:
        convert both nums1 and nums2 to set. 

        then traverse over nums1, check if num in nums2, not then add it to list. 
        do the same for nums2. 
        '''

        nums1_set = set(nums1)
        nums2_set = set(nums2)
        ans1 = []
        ans2 = []

        def get_diff(nums1, nums2):
            ans = []
            for num in nums1:
                if num not in nums2:
                    ans.append(num)
            
            return ans
        
        return [get_diff(nums1_set, nums2_set), get_diff(nums2_set, nums1_set)]

        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        
        '''
        
        