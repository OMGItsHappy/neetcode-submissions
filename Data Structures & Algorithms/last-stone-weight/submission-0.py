import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)

            newStone = abs(stone1 - stone2)
            if newStone:
                heapq.heappush(heap, -newStone)

        return -heapq.heappop(heap) if len(heap) > 0 else 0