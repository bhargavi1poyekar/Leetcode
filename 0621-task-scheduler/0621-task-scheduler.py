class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count=[0 for i in range(26)]
        for i in tasks:
            count[ord(i)-ord('A')]+=1
        count.sort()

        max_count=count.pop()
        idle=(max_count-1)*n

        while idle>0 and count:
            idle-=min((max_count-1),count.pop())
        idle=max(0,idle)
        return idle+len(tasks)

        