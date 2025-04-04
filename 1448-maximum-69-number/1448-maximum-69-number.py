class Solution:
    def maximum69Number (self, num: int) -> int:
        
        orig_num = num
        num = str(num)

        for i in range(len(num)):
            if num[i] == '6':
                num = num[:i] + '9' + num[i+1:]
                return int(num)

        return orig_num