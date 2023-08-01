class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        
        
        def binary_search(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        
        height_to_lengths = defaultdict(list)
        for length, height in rectangles:
            height_to_lengths[height].append(length)
        
        # print(height_to_lengths)
        
        max_height=max(height_to_lengths.keys())
        ans=[]

        for lengths in height_to_lengths.values():
            lengths.sort()

        # print(height_to_lengths)
        # print(max_height)

        for x,y in points:
            count=0
            # print(x,y)
            for height in range(y,max_height+1):
                # print(height)
                if height in height_to_lengths.keys():
                    # print(height, x)
                    # print(len(height_to_lengths[height]))
                    # print(f'x:{x}')
                    # print(binary_search(height_to_lengths[height],x))
                    count+=len(height_to_lengths[height])-binary_search(height_to_lengths[height],x)
        
            ans.append(count)
        return ans

        

        