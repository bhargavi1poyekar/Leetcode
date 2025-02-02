class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []

        for pos, spd in sorted(zip(position, speed))[::-1]:
            distance = target - pos
            time = distance // spd

            if stack and stack[-1] < time:
                stack.append(time)
            elif not stack:
                stack.append(time)
        
        return len(stack)


