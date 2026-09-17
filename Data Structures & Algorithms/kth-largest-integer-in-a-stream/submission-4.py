import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.list = nums
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if k < len(heap):
                heapq.heappop(heap)
        self.heap = heap
        self.k = k
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if self.k < len(self.heap):
            heapq.heappop(self.heap)
        return self.heap[0]
        
