class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(string_num, target):
            if not string_num and target == 0:
                return True

            # Invalid Partition Found
            if target < 0:
                return False

            # Recursively check all partitions for a valid partition
            for index in range(len(string_num)):
                left = string_num[: index + 1]
                right = string_num[index + 1 :]
                left_num = int(left)

                if can_partition(right, target - left_num):
                    return True

            return False

        
        punishment_no = 0
        for i in range(1, n+1):
            num_square = i*i
            if can_partition(str(num_square), i):
                punishment_no += num_square
        
        return punishment_no
                
