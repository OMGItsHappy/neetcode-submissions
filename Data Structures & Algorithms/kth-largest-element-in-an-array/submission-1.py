import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        numsLen = len(nums)
        while nums:
            heapq.heappush(heap,  nums.pop())
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]