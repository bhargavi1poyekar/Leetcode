class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater_nums2 = {}

        for num in nums2:
            while stack and stack[-1] < num:
                greater_nums2[stack.pop()] = num
            stack.append(num)
        
        greater_arr = []
        for num in nums1:
            if num in greater_nums2:
                greater_arr.append(greater_nums2[num])
            else:greater_arr.append(-1)
        
        return greater_arr

