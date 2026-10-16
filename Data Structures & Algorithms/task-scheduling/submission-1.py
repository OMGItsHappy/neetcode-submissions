from heapq import heappush, heappop

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int)
        total = len(tasks)

        for task in tasks:
            counts[task] += 1
        
        heap = []
        for key, value in counts.items():
            heappush(heap, -value)
        
        time = 0
        cooldowns = []
        while heap or cooldowns:
            time += 1
            if heap:
                val = heappop(heap) + 1
                if val < 0:
                    cooldowns.append((val, time + n))
            if cooldowns:
                if cooldowns[0][1] <= time:
                    heappush(heap, cooldowns.pop(0)[0])
        return time
            

