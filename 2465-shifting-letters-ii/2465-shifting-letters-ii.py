class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        n = len(s)
        diff_arr = [0] * (n + 1)

        for shiftOp in shifts:
            start, end, direction = shiftOp
            diff_arr[start] += (1 if direction == 1 else -1)
            if end + 1 < n:
                diff_arr[end + 1] -= (1 if direction == 1 else -1)

        currentShift = 0
        shiftList = list(s)
        for i in range(n):
            currentShift += diff_arr[i]
            netShift = (currentShift % 26 + 26) % 26
            shiftList[i] = chr((ord(shiftList[i]) - ord('a') + netShift) % 26 + ord('a'))

        return ''.join(shiftList)