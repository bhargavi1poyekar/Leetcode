class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        hash_string = Counter(arr)
        order_count = 0

        for i in arr:
            if hash_string[i] == 1:
                # print(i)
                order_count += 1

                if order_count == k:
                    return i
                

        return ""