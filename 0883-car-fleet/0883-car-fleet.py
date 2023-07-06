class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack=[]

        for position, speed in sorted(zip(position,speed))[::-1]:

            distance=target-position
            time=distance/speed
            if not stack:
                stack.append(time)
            elif time>stack[-1]:
                stack.append(time)
        
        return len(stack)