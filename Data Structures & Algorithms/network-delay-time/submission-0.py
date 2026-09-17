class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for source, target, weight in times:
            edges[source].append((target, weight))

        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            weight, target = heapq.heappop(minHeap)
            if target in visit:
                continue
            visit.add(target)
            t = weight

            for adjacentTarget, adjacentWeight in edges[target]:
                if adjacentTarget not in visit:
                    heapq.heappush(minHeap, (weight + adjacentWeight, adjacentTarget))
        return t if len(visit) == n else -1


        